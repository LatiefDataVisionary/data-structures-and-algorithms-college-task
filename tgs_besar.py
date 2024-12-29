import datetime
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def pilih_tanggal():
    date_picker = widgets.DatePicker(
        description='Pilih Tanggal',
        disabled=False
    )
    display(date_picker)

    button = widgets.Button(description="Pilih")
    output = widgets.Output()
    
    def on_button_clicked(b):
        with output:
            selected_date = date_picker.value
            if selected_date:
                print(f"Tanggal yang dipilih: {selected_date}")
                global tanggal_terpilih
                tanggal_terpilih = selected_date
                button.close()
            else:
                print("Tanggal belum dipilih.")
    
    button.on_click(on_button_clicked)
    display(button, output)

def tambah_tugas(tugas):
    judul = input("Masukkan judul tugas: ")
    deskripsi = input("Masukkan deskripsi tugas: ")
    kategori = input("Masukkan kategori tugas (misalnya: Matematika, Proyek, Ujian, dll.): ")
    prioritas = input("Masukkan prioritas tugas (tinggi, sedang, rendah): ")
    
    global tanggal_terpilih
    tanggal_terpilih = None
    pilih_tanggal()
    
    # Tunggu sampai tanggal dipilih
    while tanggal_terpilih is None:
        pass

    waktu_deadline_str = input("Masukkan waktu deadline (HH:MM): ")
    waktu_deadline = datetime.datetime.strptime(f"{tanggal_terpilih} {waktu_deadline_str}", "%Y-%m-%d %H:%M")
    
    tugas_baru = {
        'judul': judul,
        'deskripsi': deskripsi,
        'kategori': kategori,
        'prioritas': prioritas,
        'waktu_deadline': waktu_deadline,
        'status': 'belum selesai'
    }
    tugas.append(tugas_baru)
    print(f"Tugas '{judul}' telah ditambahkan.")

def lihat_tugas(tugas):
    if not tugas:
        print("Tidak ada tugas yang ditambahkan.")
        return
    for idx, t in enumerate(tugas):
        status = t['status']
        deadline = t['waktu_deadline'].strftime("%Y-%m-%d %H:%M")
        print(f"{idx + 1}. [{status}] {t['judul']} - {t['kategori']} - Prioritas: {t['prioritas']} - Batas waktu: {deadline} - Deskripsi: {t['deskripsi']}")

def tandai_selesai(tugas):
    lihat_tugas(tugas)
    index = int(input("Masukkan nomor tugas yang sudah selesai: ")) - 1
    if 0 <= index < len(tugas):
        tugas[index]['status'] = 'selesai'
        print(f"Tugas '{tugas[index]['judul']}' telah ditandai sebagai selesai.")
    else:
        print("Nomor tugas tidak valid.")

def peringatan_tugas(tugas):
    sekarang = datetime.datetime.now()
    for t in tugas:
        if t['status'] == 'belum selesai':
            waktu_tersisa = (t['waktu_deadline'] - sekarang).total_seconds()
            if 0 < waktu_tersisa <= 86400:  # 86400 detik = 24 jam
                print(f"Peringatan! Tugas '{t['judul']}' mendekati batas waktu (kurang dari 24 jam).")

def statistik_tugas(tugas, periode='hari'):
    sekarang = datetime.datetime.now()
    
    if periode == 'hari':
        batas_waktu = sekarang - datetime.timedelta(days=1)
    elif periode == 'minggu':
        batas_waktu = sekarang - datetime.timedelta(weeks=1)
    elif periode == 'bulan':
        batas_waktu = sekarang - datetime.timedelta(days=30)
    elif periode == 'tahun':
        batas_waktu = sekarang - datetime.timedelta(days=365)
    else:
        print("Periode tidak valid.")
        return
    
    tugas_dalam_periode = [t for t in tugas if t['waktu_deadline'] >= batas_waktu]
    total = len(tugas_dalam_periode)
    selesai = sum(1 for t in tugas_dalam_periode if t['status'] == 'selesai')
    belum_selesai = total - selesai
    
    print(f"\nStatistik Tugas untuk periode {periode}:")
    print(f"Total tugas: {total}")
    print(f"Tugas selesai: {selesai}")
    print(f"Tugas belum selesai: {belum_selesai}")

    labels = ['Selesai', 'Belum Selesai']
    sizes = [selesai, belum_selesai]
    colors = ['#4CAF50', '#FF5733']
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, startangle=90, counterclock=False, wedgeprops=dict(width=0.3))
    ax.set(aspect="equal")
    plt.title(f"Donut Chart Tingkat Penyelesaian Tugas ({periode})")
    plt.show()

def edit_tugas(tugas):
    lihat_tugas(tugas)
    index = int(input("Masukkan nomor tugas yang ingin diedit: ")) - 1
    if 0 <= index < len(tugas):
        t = tugas[index]
        print("Masukkan detail baru (tekan Enter untuk mempertahankan nilai lama):")
        judul = input(f"Judul ({t['judul']}): ")
        deskripsi = input(f"Deskripsi ({t['deskripsi']}): ")
        kategori = input(f"Kategori ({t['kategori']}): ")
        prioritas = input(f"Prioritas ({t['prioritas']}): ")
        tanggal_str = input(f"Deadline ({t['waktu_deadline'].strftime('%Y-%m-%d %H:%M')}): ")

        if judul:
            t['judul'] = judul
        if deskripsi:
            t['deskripsi'] = deskripsi
        if kategori:
            t['kategori'] = kategori
        if prioritas:
            t['prioritas'] = prioritas
        if tanggal_str:
            t['waktu_deadline'] = datetime.datetime.strptime(tanggal_str, "%YYYY-%mm-%dd %H:%M")
        
        print(f"Tugas '{t['judul']}' telah diperbarui.")
    else:
        print("Nomor tugas tidak valid.")

def main():
    tugas = []

    while True:
        peringatan_tugas(tugas)
        
        print("\nMenu:")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Tandai tugas sebagai selesai")
        print("4. Edit tugas")
        print("5. Lihat statistik tugas")
        print("6. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            tambah_tugas(tugas)
        elif pilihan == '2':
            lihat_tugas(tugas)
        elif pilihan == '3':
            tandai_selesai(tugas)
        elif pilihan == '4':
            edit_tugas(tugas)
        elif pilihan == '5':
            print("\nPilih periode statistik:")
            print("1. Hari")
            print("2. Minggu")
            print("3. Bulan")
            print("4. Tahun")
            periode_pilihan = input("Pilih opsi periode: ")
            if periode_pilihan == '1':
                statistik_tugas(tugas, periode='hari')
            elif periode_pilihan == '2':
                statistik_tugas(tugas, periode='minggu')
            elif periode_pilihan == '3':
                statistik_tugas(tugas, periode='bulan')
            elif periode_pilihan == '4':
                statistik_tugas(tugas, periode='tahun')
            else:
                print("Pilihan periode tidak valid.")
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    root = widgets.Output()
    display(root)
    main()