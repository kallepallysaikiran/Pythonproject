# Pythonproject
#python programming projec
# Import libraries
from tkinter import ttk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import random
from datetime import date
from datetime import datetime
root = Tk()

prices = {
    "CheeseBurger": 189,
    "Manchuria": 100,
    "Jerk Chicken": 299,
    "Paella": 180,
    "Parmigiana": 896,
    "sushi": 400,
}
root.title("Digital menu project")


# ...................functions...........
def order_button():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID :", "")
    transaction_list = orderTransaction.cget("text").split("Rs ")
    transaction_list.pop(len(transaction_list) - 1)
    order_day = date.today()
    order_time = datetime.now()

    with open(new_receipt, 'w') as file:
        file.write("FAST FOOD")
        file.write("\n")
        file.write("_________________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n\n")
        for item in transaction_list:
            file.write(item+"\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text="Total :0Rs")
    orderIDLabel.configure(text="ORDER ID: "+order_id())
    orderTransaction.configure(text="")

# generating a random order ID when started a new order


def order_id():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    order_id1 = "VSA_"
    random_letters = ""
    random_digits = ""
    for i in range(0, 6):
        random_letters += random.choice(letters)
        random_letters += random.choice(letters)
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))
        random_digits += str(random.choice(numbers))
        random_digits += str(random.choice(numbers))
        order_id1 += random_letters+random_digits

        return order_id1


def display_burger():
    burgerDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"

    )

    manchurianDishFrame.configure(style="DishFrame.TFrame")
    jerkChickenDishFrame.configure(style="DishFrame.TFrame")
    paellaDishFrame.configure(style="DishFrame.TFrame")
    ParmigianaDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=burgerImage,
        text="CheeseBurger",
        font=('Helvetica', 14, "bold"),
        foreground="white", compound="bottom",
        padding=(5, 5, 5, 5),
    )


def display_manchuria():
    manchurianDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"

    )
    burgerDishFrame.configure(style="DishFrame.TFrame")

    jerkChickenDishFrame.configure(style="DishFrame.TFrame")
    paellaDishFrame.configure(style="DishFrame.TFrame")
    ParmigianaDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=chickenManchurianImage,
        text="Manchuria",
        font=('Helvetica', 14, "bold"),
        foreground="white", compound="bottom",
        padding=(5, 5, 5, 5),


    )


def display_chicken():
    jerkChickenDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"

    )
    burgerDishFrame.configure(style="DishFrame.TFrame")
    manchurianDishFrame.configure(style="DishFrame.TFrame")

    paellaDishFrame.configure(style="DishFrame.TFrame")
    ParmigianaDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=jerkChickenImage,
        text="Jerk Chicken",
        font=('Helvetica', 14, "bold"),
        foreground="white", compound="bottom",
        padding=(5, 5, 5, 5),


    )


def display_paella():
    paellaDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"

    )
    burgerDishFrame.configure(style="DishFrame.TFrame")
    manchurianDishFrame.configure(style="DishFrame.TFrame")
    jerkChickenDishFrame.configure(style="DishFrame.TFrame")

    ParmigianaDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=paellaImage,
        text="Paella",
        font=('Helvetica', 14, "bold"),
        foreground="white", compound="bottom",
        padding=(5, 5, 5, 5),


    )


def display_parmigiana():
    ParmigianaDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"

    )
    burgerDishFrame.configure(style="DishFrame.TFrame")
    manchurianDishFrame.configure(style="DishFrame.TFrame")
    jerkChickenDishFrame.configure(style="DishFrame.TFrame")
    paellaDishFrame.configure(style="DishFrame.TFrame")

    sushiDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=ParmigianaImage,
        text="Parmigiana",
        font=('Helvetica', 14, "bold"),
        foreground="white", compound="bottom",
        padding=(5, 5, 5, 5),


    )


def display_sushi():
    sushiDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"

    )
    burgerDishFrame.configure(style="DishFrame.TFrame")
    manchurianDishFrame.configure(style="DishFrame.TFrame")
    jerkChickenDishFrame.configure(style="DishFrame.TFrame")
    paellaDishFrame.configure(style="DishFrame.TFrame")
    ParmigianaDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=sushiImage,
        text="sushi",
        font=('Helvetica', 14, "bold"),
        foreground="white", compound="bottom",
        padding=(5, 5, 5, 5),
     )


def add():
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text")+"....."+str(prices[displayLabel.cget("text")])+"Rs "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # updating the order total label

    order_total = orderTotalLabel.cget("text").replace("Total :", "")
    order_total = order_total.replace("Rs", "")
    updated_total = int(order_total)+prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="Total :"+str(updated_total)+"Rs ")


def remove():
    dish_to_remove = displayLabel.cget("text")+"....."+str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("Rs ")
    transaction_list.pop(len(transaction_list)-1)

    if dish_to_remove in transaction_list:

        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item+"Rs "
        orderTransaction.configure(text=updated_order)
        order_total = orderTotalLabel.cget("text").replace("Total :", "")
        order_total = order_total.replace("Rs", "")
        updated_total = int(order_total)-prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="Total :"+str(updated_total)+"Rs ")

# ...............styling and images


s = ttk.Style()

s.configure('MainFrame.TFrame', background="#2B2B28")

s.configure('MenuFrame.TFrame', background="#4A4A48")

s.configure('DisplayFrame.TFrame', background="#0F1110")

s.configure('OrderFrame.TFrame', background="#B7C4CF")

s.configure('DishFrame.TFrame', backened="#4A4A48", relief="raised")

s.configure('SelectedDish.TFrame', background="#C6F7B0")

s.configure('MenuLabel.TLabel',
            background="#0F1110",
            font=("Arial", 13, "italic"),
            foreground='white',

            padding=(5, 5, 5, 5),
            width=21
            )

s.configure('orderTotalLabel.TLabel',
            background="#0F1110",
            font=("Arial", 10, "bold"),
            foreground="white",
            padding=(2, 2, 2, 2),
            anchor="w"
            )

s.configure('orderTransaction.TLabel',
            background="#4A4A48",
            font=('Helvetica', 12),
            foreground="white",
            wraplength=170,
            anchor="nw",
            padding=(3, 3, 3, 3)
            )

# images


LogoImageObject = Image.open("images/logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("images/view.jpeg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# adding images in menu function

displayDefaultImageObject = Image.open("images/Presentation1.jpg").resize((350, 360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

burgerImageObject = Image.open("images/menu/burger.jpeg").resize((350, 334))
burgerImage = ImageTk.PhotoImage(burgerImageObject)

chickenManchurianImageObject = Image.open("images/menu/chicken manchurian.jpeg").resize((350, 334))
chickenManchurianImage = ImageTk.PhotoImage(chickenManchurianImageObject)

jerkChickenImageObject = Image.open("images/menu/jerk chicken1.png").resize((350, 334))
jerkChickenImage = ImageTk.PhotoImage(jerkChickenImageObject)

paellaImageObject = Image.open("images/menu/paella1.jpg").resize((350, 334))
paellaImage = ImageTk.PhotoImage(paellaImageObject)

ParmigianaImageObject = Image.open("images/menu/Parmigiana.jpeg").resize((350, 334))
ParmigianaImage = ImageTk.PhotoImage(ParmigianaImageObject)

sushiImageObject = Image.open("images/menu/sushi1.png").resize((350, 334))
sushiImage = ImageTk.PhotoImage(sushiImageObject)

# ..................widgets
# creating a main frame
mainFrame = ttk.Frame(root, width=800, height=580, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")

# adding frames in main frame

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, sticky="NSEW", columnspan=3)

menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style="DisplayFrame.TFrame")
displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")

orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky="NSEW")


# adding dish frames in menu Frame


burgerDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
burgerDishFrame.grid(row=1, column=0, sticky="NEWS")

manchurianDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
manchurianDishFrame.grid(row=2, column=0, sticky="NEWS")

jerkChickenDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
jerkChickenDishFrame.grid(row=3, column=0, sticky="NEWS")


paellaDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
paellaDishFrame.grid(row=4, column=0, sticky="NEWS")


ParmigianaDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
ParmigianaDishFrame.grid(row=5, column=0, sticky="NEWS")


sushiDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
sushiDishFrame.grid(row=6, column=0, sticky="NEWS")

# labels main widget

LogoLabel = ttk.Label(topBannerFrame, image=LogoImage, background="#0F1110")
LogoLabel.grid(row=0, column=0, sticky="N")


RestaurantBannerLabel = ttk.Label(topBannerFrame, image=TopBannerImage, background="#0F1110")
RestaurantBannerLabel.grid(row=0, column=1, sticky="NSEW")

# region menu section
MainMenuLabel = ttk.Label(menuFrame, text="MENU", style="MenuLabel.TFrame")
MainMenuLabel.grid(row=0, column=0, sticky="we")
MainMenuLabel.configure(
    anchor="center",
    font=("Helvetica", 14, "bold")

)
burgerDishLabel = ttk.Label(burgerDishFrame, text="Cheese burger.....189RS", style="MenuLabel.TLabel")
burgerDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

chickenManchurianDishLabel = ttk.Label(manchurianDishFrame, text="Chicken Manchuria.80RS", style="MenuLabel.TLabel")
chickenManchurianDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

jerkChickenDishLabel = ttk.Label(jerkChickenDishFrame, text="Jerk Chicken.....299Rs", style="MenuLabel.TLabel")
jerkChickenDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

paellaDishLabel = ttk.Label(paellaDishFrame, text="Paella.....180Rs", style="MenuLabel.TLabel")
paellaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

ParmigianaDishLabel = ttk.Label(ParmigianaDishFrame, text="Parmigiana.....896Rs", style="MenuLabel.TLabel")
ParmigianaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

sushiDishLabel = ttk.Label(sushiDishFrame, text="sushi.....400Rs", style="MenuLabel.TLabel")
sushiDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

# >.................buttons
burgerDishPlayButton = ttk.Button(burgerDishFrame, text="Display", command=display_burger)
burgerDishPlayButton.grid(row=0, column=1, padx=10)

chickenManchurianDishPlayButton = ttk.Button(manchurianDishFrame, text="Display", command=display_manchuria)
chickenManchurianDishPlayButton.grid(row=0,  column=1, padx=10)

jerkChickenDishButton = ttk.Button(jerkChickenDishFrame, text="Display", command=display_chicken)
jerkChickenDishButton.grid(row=0, column=1, padx=10)

paellaDishButton = ttk.Button(paellaDishFrame, text="Display", command=display_paella)
paellaDishButton.grid(row=0, column=1, padx=10)

ParmigianaDishButton = ttk.Button(ParmigianaDishFrame, text="Display", command=display_parmigiana)
ParmigianaDishButton.grid(row=0, column=1, padx=10)

sushiDishButton = ttk.Button(sushiDishFrame, text="Display", command=display_sushi)
sushiDishButton.grid(row=0, column=1, padx=10)


# region display section
displayLabel = ttk.Label(displayFrame, image=displayDefaultImage)

displayLabel.grid(row=0, column=0, sticky="NSEW", columnspan=2)

displayLabel.configure(background="#0F1110")


addOrderButton = ttk.Button(displayFrame, text="ADD TO ORDER", command=add)
addOrderButton.grid(row=1, column=0, padx=2, sticky="NSEW")
removeOrderButton = ttk.Button(displayFrame, text="REMOVE", command=remove)
removeOrderButton.grid(row=1, column=1, padx=10, sticky="NSEW")

# order section

orderTitleLabel = ttk.Label(orderFrame, text="ORDER")
orderTitleLabel.configure(
    foreground='white', background='Black',
    font=("Helvetica", 14, "bold"), anchor="center",
    padding=(5, 5, 5, 5),
)
orderTitleLabel.grid(row=0, column=0, sticky="EW")


orderIDLabel = ttk.Label(orderFrame, text="ORDER ID :"+order_id())
orderIDLabel.configure(
    background="black", foreground="white",
    font=("Helvetica", 11, "italic"), anchor="w"

)
orderIDLabel.grid(row=1, column=0, sticky="EW", pady=1)

orderTransaction = ttk.Label(orderFrame, style='orderTransaction.TLabel')
orderTransaction.grid(row=2, column=0, sticky="NSEW")


orderTotalLabel = ttk.Label(orderFrame, text="Total :0Rs", style="orderTotalLabel.TLabel")
orderTotalLabel.grid(row=3, column=0, sticky="EW")
orderButton = ttk.Button(orderFrame, text="ORDER", command=order_button)
orderButton.grid(row=4, column=0, sticky="EW")

# '''''''''grid configuration

mainFrame.columnconfigure(2, weight=1)
mainFrame.rowconfigure(1, weight=1
                       )
menuFrame.columnconfigure(0, weight=1)
menuFrame.rowconfigure(1, weight=1)
menuFrame.rowconfigure(2, weight=1)
menuFrame.rowconfigure(3, weight=1)
menuFrame.rowconfigure(4, weight=1)
menuFrame.rowconfigure(5, weight=1)
menuFrame.rowconfigure(6, weight=1)
orderFrame.columnconfigure(0, weight=1)
orderFrame.rowconfigure(2, weight=1)
root.mainloop()
