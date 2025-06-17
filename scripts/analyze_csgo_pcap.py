# scripts/analyze_csgo_pcap.py

import sys
import os
from scapy.all import rdpcap, IP, UDP, TCP
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_csgo_pcap(pcap_file_path):
    """
    CS:GO ağ trafiğini analiz eder ve temel istatistikleri görselleştirir.
    """
    if not os.path.exists(pcap_file_path):
        print(f"Hata: '{pcap_file_path}' dosyası bulunamadı.")
        sys.exit(1)

    print(f"'{pcap_file_path}' dosyasından paketler okunuyor...")
    try:
        packets = rdpcap(pcap_file_path)
    except Exception as e:
        print(f"Paketler okunurken hata oluştu: {e}")
        sys.exit(1)

    print(f"Toplam {len(packets)} paket okundu.")

    csgo_traffic = []
    
    # CS:GO ile ilişkili yaygın portlar (UDP ve TCP)
    # SDR (Steam Datagram Relay) ve diğer bilinen portlar
    CSGO_UDP_PORTS = list(range(27000, 27201)) + [4380] # Geniş aralık, SDR ve ses
    CSGO_TCP_PORTS = [27015, 27036] # Genel oyun ve istemci

    for pkt in packets:
        if IP in pkt:
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            protocol = None
            src_port = None
            dst_port = None
            payload_len = len(pkt[IP].payload)

            if UDP in pkt:
                protocol = 'UDP'
                src_port = pkt[UDP].sport
                dst_port = pkt[UDP].dport
                if (src_port in CSGO_UDP_PORTS or dst_port in CSGO_UDP_PORTS):
                    csgo_traffic.append({
                        'Source IP': src_ip,
                        'Destination IP': dst_ip,
                        'Protocol': protocol,
                        'Source Port': src_port,
                        'Destination Port': dst_port,
                        'Packet Length': len(pkt),
                        'Payload Length': payload_len
                    })
            elif TCP in pkt:
                protocol = 'TCP'
                src_port = pkt[TCP].sport
                dst_port = pkt[TCP].dport
                if (src_port in CSGO_TCP_PORTS or dst_port in CSGO_TCP_PORTS):
                    csgo_traffic.append({
                        'Source IP': src_ip,
                        'Destination IP': dst_ip,
                        'Protocol': protocol,
                        'Source Port': src_port,
                        'Destination Port': dst_port,
                        'Packet Length': len(pkt),
                        'Payload Length': payload_len
                    })
    
    if not csgo_traffic:
        print("Belirtilen CS:GO portlarında trafik bulunamadı.")
        return

    df = pd.DataFrame(csgo_traffic)
    print("\nCS:GO Trafiği Özeti:")
    print(df.head())
    print(f"\nToplam CS:GO ile ilgili paket sayısı: {len(df)}")
    print(f"Toplam CS:GO ile ilgili veri boyutu (byte): {df['Packet Length'].sum()} KB: {df['Packet Length'].sum()/1024:.2f} MB: {df['Packet Length'].sum()/(1024*1024):.2f}")

    # En çok trafik olan hedef IP'ler
    top_dst_ips = df.groupby('Destination IP')['Packet Length'].sum().nlargest(10).reset_index()
    top_dst_ips['Packet Length (MB)'] = top_dst_ips['Packet Length'] / (1024 * 1024)

    print("\nEn Çok Trafik Olan Hedef IP Adresleri (İlk 10):")
    print(top_dst_ips)

    # Protokol Dağılımı
    protocol_counts = df['Protocol'].value_counts(normalize=True) * 100
    print("\nProtokol Dağılımı (%):")
    print(protocol_counts)

    # Görselleştirmeler
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Destination IP', y='Packet Length (MB)', data=top_dst_ips)
    plt.title('En Çok Trafik Giden CS:GO Hedef IP Adresleri (MB)')
    plt.xlabel('Hedef IP Adresi')
    plt.ylabel('Trafik Miktarı (MB)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('csgo_top_dst_ips.png')
    print("\n'csgo_top_dst_ips.png' dosyası kaydedildi.")
    plt.close()

    plt.figure(figsize=(8, 8))
    plt.pie(protocol_counts, labels=protocol_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    plt.title('CS:GO Trafiği Protokol Dağılımı')
    plt.tight_layout()
    plt.savefig('csgo_protocol_distribution.png')
    print("'csgo_protocol_distribution.png' dosyası kaydedildi.")
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python analyze_csgo_pcap.py <pcap_dosya_yolu>")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    analyze_csgo_pcap(pcap_file)
