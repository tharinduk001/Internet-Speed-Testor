import builtins
import speedtest
import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="superhero")
window.title('Speed Testor')
window.geometry('345x460')
window.resizable(False, False)

download_int = tk.IntVar()
download_txr = tk.StringVar()
upload_int = tk.IntVar() 
upload_txr = tk.StringVar()
ping_int = tk.IntVar()
ping_txt = tk.StringVar()


title_label = ttk.Label(master=window, text="Internet Speed Tester",
                        font="Arial 23 bold", style="primary")
title_label.pack(pady=10)


def themechanger(i):
    title_label.configure(bootstyle=i)
    download_label.configure(bootstyle=i)
    upload_label.configure(bootstyle=i)
    ping_label.configure(bootstyle=i)
    start_button.configure(bootstyle=i)
    output_label.configure(bootstyle=i)
    my_menu.configure(bootstyle=i)
    my_meter.configure(bootstyle=i)


def start():
    try:
        test = speedtest.Speedtest()

        test.get_servers()
        msgtxt = "Loading Server List..."
        # print(msgtxt)

        best = test.get_best_server()
        msgtxt = "Loading Best Server..."
        # print(msgtxt)

        # print(f"Found {best['host']} located in {best['country']}")

        download_r = test.download()
        # print("Performing download test...")
        upload_r = test.upload()
        # print("Performing upload test...")
        ping_r = test.results.ping
        # print("Performing ping test...")

        download_int = downloadSpeed = "%.2f" % (download_r / 1024**2)
        upload_int = uploadSpeed = "%.2f" % (upload_r / 1024**2)
        ping_int = ping = "%.2f" % ping_r

        download_txr.set(f"{download_int} Mbps")
        upload_txr.set(f"{upload_int} Mbps")
        ping_txt.set(f"{ping_int} ms")

        # print(f"Download Speed : {downloadSpeed}")
        # print(f"Upload Speed : {uploadSpeed}")
        # print(f"Ping : {ping}")

        # adding results to meter widget
        output_label.config(text="Process Finished")
        my_meter.configure(amountused=download_int)

    except Exception as e:
        output_label.config(text=e)
        # print("Something went wrong : ", e)


my_meter = ttk.Meter(window, bootstyle="danger", subtext=f"Download Speed", subtextfont="Calbri 12 bold",
                     textright="Mbps", interactive=True, amounttotal=60, subtextstyle="", metertype="semi", stripethickness=7)
my_meter.pack(pady=5)

# creating different frame with output values
input_frame = ttk.Frame(master=window)
input_frame.pack(pady=12)

download_label = ttk.Label(
    master=input_frame, text="Download", font="Calibri 14 bold", style="primary")
download_label.grid(row=0, column=0, padx=23)

upload_label = ttk.Label(master=input_frame, text="Upload",
                         font="Calibri 14 bold", style="primary")
upload_label.grid(row=0, column=1, padx=23)

ping_label = ttk.Label(master=input_frame, text="Ping",
                       font="Calibri 14 bold", style="primary")
ping_label.grid(row=0, column=2, padx=23)

download_label_value = ttk.Label(
    master=input_frame, text="", font="Calibri 14 bold", style="info", textvariable=download_txr)
download_label_value.grid(row=1, column=0, padx=10)

upload_label_value = ttk.Label(master=input_frame, text="",
                               font="Calibri 14 bold", style="info", textvariable=upload_txr)
upload_label_value.grid(row=1, column=1, padx=10)

ping_label_value = ttk.Label(master=input_frame, text="",
                             font="Calibri 14 bold", style="info", textvariable=ping_txt)
ping_label_value.grid(row=1, column=2, padx=10)

start_button = ttk.Button(window, text="GO !", width=10,
                          style="danger outlined", command=start)
start_button.pack(pady=20)

# creating label widget
input_frame2 = ttk.Frame(master=window)
input_frame2.pack(pady=5)

outputString = "Press Go Button and wait about 30s."
output_label = ttk.Label(
    master=input_frame2, text="Press Go Button and wait about 30s...", font="Calibri 10 italic", style="info")
output_label.grid(row=0, column=0, padx=12)

my_menu = ttk.Menubutton(
    master=input_frame2, bootstyle="info", text="theme", width=6)
my_menu.grid(row=0, column=1, padx=20)

themelist = ttk.Menu(my_menu)

item_var = ttk.StringVar()
for i in ['primary', 'success', 'warning', 'danger']:
    themelist.add_radiobutton(
        label=i, variable=item_var, command=lambda i=i: themechanger(i))

my_menu['menu'] = themelist

window.mainloop()
