from tkinter import *
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

window = Tk()
window.geometry("1500x700")
window.title("Banknote Authentication")
window.configure(bg="#f0f2f5")

from MyDecTreeClass import MyDecisionTree
decisionTree = MyDecisionTree()

# ---------------- Functions ----------------
def trainData():
    newSeedValue = int(seedsVar.get())
    decisionTree.updateSeed(newSeedValue)
    decisionTree.trainData()

    text.delete("1.0", "end")
    text.insert(END, "data trained")

def testData():
    text.delete("1.0","end")
    text.insert(END, decisionTree.readCategories())
    result, accuracy = decisionTree.testData()

    text.insert(END, '\n['+str(result[0]))
    text.insert(END, '\n '+str(result[1]) +']')
    text.insert(END, '\n\nAccuracy ' + str(int(accuracy*100)) + '%')

def makeNewPrediction():
    variance = float(entry41.get())
    skewness = float(entry42.get())
    curtosis = float(entry43.get())
    entropy = float(entry44.get())
    prediction_Res = decisionTree.makePrediction(variance, skewness, curtosis, entropy)
    entry45.delete(0, END)
    entry45.insert(END, prediction_Res)

    if prediction_Res.lower() == "real":
        canvas.itemconfig(current_image, image=real_img)
    else:
        canvas.itemconfig(current_image, image=forged_img)

    history_table.insert(
        "", END,
        values=(variance, skewness, curtosis, entropy, prediction_Res)
    )



def showFeatureImportance():
    if decisionTree.tree is None:
        messagebox.showerror("Error", "Train the model first.")
        return

    importance = decisionTree.tree.feature_importances_
    features = decisionTree.X.columns

    plt.figure(figsize=(7, 4))
    plt.bar(features, importance)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.title("Decision Tree Feature Importance", fontsize=14, fontweight='bold')
    plt.xlabel("Features")
    plt.ylabel("Importance")
    plt.tight_layout()
    plt.show()

# ---------------- Header ----------------
Label(
    window,
    text="Banknote Authentication System",
    font=("Verdana", 20, "bold"),
    bg="#f0f2f5",
    fg="#003366"
).pack(pady=20)

# ---------------- Main Layout Frames (Left / Right Columns) ----------------
main_frame = Frame(window, bg="#f0f2f5")
main_frame.pack(fill=BOTH, expand=True)

left_frame = Frame(main_frame, bg="#f0f2f5")
right_frame = Frame(main_frame, bg="#f0f2f5")

left_frame.pack(side=LEFT, padx=20)
right_frame.pack(side=RIGHT, padx=20)

# ---------------- Left Column (Training + Testing + Image) ----------------
# --- Training/Test Frame ---
frame_top = Frame(left_frame, bg="white", bd=3, relief=GROOVE)
frame_top.pack(padx=10, pady=10)

Label(frame_top, text="Random Seed Value", font=("Arial", 12, "bold"), bg="white")\
    .grid(row=0, column=0, padx=10, pady=10)

list1 = ['1', '2', '3', '4', '5','6','7','8','9']
seedsVar = StringVar(value="1")
OptionMenu(frame_top, seedsVar, *list1)\
    .grid(row=0, column=1, padx=10, pady=10)

Button(frame_top, text="Train Data", command=trainData,
       bg="#d9eaff", font=("Arial", 11, "bold"))\
       .grid(row=1, column=0, sticky="ew", padx=10, pady=10)

Button(frame_top, text="Test Data", command=testData,
       bg="#d9eaff", font=("Arial", 11, "bold"))\
       .grid(row=1, column=1, sticky="ew", padx=10, pady=10)

Button(frame_top, text="Feature Importance",
       command=showFeatureImportance,
       bg="#ffe6cc", font=("Arial", 11, "bold"))\
       .grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

Label(frame_top, text="Output", font=("Arial", 12, "bold"), bg="white")\
    .grid(row=2, column=0, pady=10)

text = Text(frame_top, height=10, width=40, font=("Consolas", 10))
text.grid(row=2, column=1, padx=10, pady=10)

# --- Image Frame ---
image_frame = Frame(left_frame, bg="#f0f2f5")
image_frame.pack(pady=20)

canvas = Canvas(image_frame, width=600, height=450, bg="#f0f2f5", highlightthickness=0)
canvas.pack()

image = PhotoImage(file="Dollar.png")
real_img = PhotoImage(file="realdollar.png")
forged_img = PhotoImage(file="fake dollar.png")

current_image = canvas.create_image(0, 0, anchor='nw', image=real_img)

# ---------------- Right Column (New Prediction Panel) ----------------




history_frame = Frame(right_frame, bg="white", bd=3, relief=RIDGE)
history_frame.pack(padx=10, pady=10, fill="both", expand=True)

Label(history_frame, text="Prediction History",
      font=("Arial", 13, "bold"), bg="white")\
      .pack(pady=5)

# Scrollable table
cols = ("Variance", "Skewness", "Curtosis", "Entropy", "Result")
history_table = ttk.Treeview(history_frame, columns=cols, show="headings", height=8)

for col in cols:
    history_table.heading(col, text=col)
    history_table.column(col, width=90, anchor="center")


scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=history_table.yview)
history_table.configure(yscroll=scrollbar.set)

history_table.pack(side=LEFT, fill="both")
scrollbar.pack(side=RIGHT, fill=Y)









Label(right_frame, text="Predict New Banknote",
      font=("Verdana", 16, "bold"),
      bg="#f0f2f5", fg="#003366").pack(pady=10)


frame_mid = Frame(right_frame, bg="white", bd=3, relief=RIDGE)
frame_mid.pack(padx=10, pady=10)

# Input fields
fields = ["Variance", "Skewness", "Curtosis", "Entropy"]
entries = []

Label(frame_mid, text="Enter Features", font=("Arial", 13, "bold"), bg="white")\
    .grid(row=0, column=0, columnspan=2, pady=10)

Label(frame_mid, text="Variance", font=("Arial", 11), bg="white").grid(row=1, column=0, pady=8, sticky="w")
entry41 = Entry(frame_mid, width=20); entry41.grid(row=1, column=1, padx=10)

Label(frame_mid, text="Skewness", font=("Arial", 11), bg="white").grid(row=2, column=0, pady=8, sticky="w")
entry42 = Entry(frame_mid, width=20); entry42.grid(row=2, column=1, padx=10)

Label(frame_mid, text="Curtosis", font=("Arial", 11), bg="white").grid(row=3, column=0, pady=8, sticky="w")
entry43 = Entry(frame_mid, width=20); entry43.grid(row=3, column=1, padx=10)

Label(frame_mid, text="Entropy", font=("Arial", 11), bg="white").grid(row=4, column=0, pady=8, sticky="w")
entry44 = Entry(frame_mid, width=20); entry44.grid(row=4, column=1, padx=10)

Button(frame_mid, text="Predict",
       command=makeNewPrediction,
       bg="#c7ffd1", font=("Arial", 12, "bold"))\
       .grid(row=5, column=0, padx=10, pady=15, sticky="ew")

entry45 = Entry(frame_mid, width=20, font=("Arial", 12, "bold"), fg="blue")
entry45.grid(row=5, column=1, padx=10, pady=15)

mainloop()
