# Παιχνίδι Κρεμάλας

# Βασικά imports
from tkinter import *  # Φέρνουμε το tkinter για να έχουμε GUI
from tkinter import messagebox as msg  # Το χρειαζόμαστε για να βγαίνουν παράθυρα μηνυμάτων
import random  # το χρειαζόμαστε για να διαλέγει το πρόγραμμα τυχαία λέξη


# Βασικό παράθυρο
main_window = Tk()  # Φτιάχνει το κυρίως παράθυρο
main_window.title("ΚΡΕΜΑΛΑ")  # Τίτλος του παραθύρου
main_window.iconbitmap("images/hangman.ico")  # Εικονίδιο του παραθύρου του παιχνιδιού
main_window.resizable(False, False)  # Το παράθυρο να μην μπορεί να αλλάξει μέγεθος

# Καθορισμός μενού παραθύρου
main_menu = Menu(main_window)  # Φτιάχνουμε widget Γενικού Μενού στο κύριο παράθυρο
main_window.config(menu=main_menu)  # Προσθέτουμε το Γενικό Μενού στο κύριο παράθυρο

# Καθορισμός υπομενού
file_menu = Menu(main_menu, tearoff=False)  # Φτιάχνουμε το υπομενού Αρχείο
difficulty_menu = Menu(main_window, tearoff=False)  # Φτιάχνουμε το υπομενού Επίπεδο Δυσκολίας

# Μενού Αρχείο
main_menu.add_cascade(label="Αρχείο", menu=file_menu)  # Προσθέτουμε το Υπομενού Αρχείο στο βασικό μενού
file_menu.add_command(label="Νέο παιχνίδι...", command=lambda: game())  # 1η εντολή για καινούριο παιχνίδι
file_menu.add_separator()  # Διαχωριστική γραμμή
file_menu.add_command(label="Έξοδος", command=main_window.quit)  # Τερματίζει το παιχνίδι

# Μενού Επίπεδο Δυσκολίας
main_menu.add_cascade(label="Επίπεδο Δυσκολίας", menu=difficulty_menu)  # Προσθέτει το Υπομενού
difficulty_menu.add_command(label="Εύκολο", command=lambda: set_difficulty(9))  # Επιλογές Δυσκολίας
difficulty_menu.add_command(label="Μεσαίο", command=lambda: set_difficulty(8))
difficulty_menu.add_command(label="Δύσκολο", command=lambda: set_difficulty(7))
difficulty_menu.add_command(label="Πολύ Δύσκολο", command=lambda: set_difficulty(6))

# Εισαγωγή του αρχείου με τις πιθανές λέξεις
with open("data/words.txt", "r", encoding="utf-8") as f:
    word_list = f.readlines()  # Το word_list είναι μια λίστα με όλες τις λέξεις που είναι στο αρχείο

# Λίστα με τις εικόνες της κρεμάλας
images = [PhotoImage(file="images/hangman0.png"), PhotoImage(file="images/hangman1.png"),
          PhotoImage(file="images/hangman2.png"), PhotoImage(file="images/hangman3.png"),
          PhotoImage(file="images/hangman4.png"), PhotoImage(file="images/hangman5.png"),
          PhotoImage(file="images/hangman6.png"), PhotoImage(file="images/hangman7.png"),
          PhotoImage(file="images/hangman8.png"), PhotoImage(file="images/hangman9.png")]

# Ορισμός global μεταβλητών
global the_word_with_spaces  # Εδώ αποθηκεύεται η λέξη με κενά ενδιάμεσα στα γράμματα
global number_of_guesses  # Μεταβλητή που αποθηκεύει τον αριθμό των λανθασμένων μαντεψιών
global the_word  # Εδώ αποθηκεύεται η λέξη
max_number_of_guesses = 6  # Αρχικοποίηση μέγιστου αριθμού μαντεψιών

# Φτιάχνουμε και κλείνουμε ένα παράθυρο για να μη βγαίνει bug στο μενού επιπέδου δυσκολίας
# και να οριστεί σωστά το top_window
top_window = Toplevel()  # Φτιάχνουμε το παράθυρο επιλογής δυσκολίας
top_window.destroy()  # Κλείνουμε το παράθυρο δυσκολίας


# Συνάρτηση για νέο παιχνίδι
def game():
    global the_word_with_spaces
    global number_of_guesses
    global the_word
    global max_number_of_guesses
    btn_dif.config(state=ACTIVE)  # Ενεργοποιεί το κουμπί επιλογής δυσκολίας
    keyboard_active(True)  # Ενεργοποίηση κουμπιών αλφαβήτου
    number_of_guesses = 0  # Αρχικοποίηση του αριθμού των μαντεψιών
    img_label.config(image=images[9 - max_number_of_guesses])  # Καθορίζει την αρχική εικόνα της κρεμάλας
    the_word = random.choice(word_list).strip("\n").upper()  # Επιλέγει τη λέξη τυχαία από τη λίστα λέξεων, αφαιρεί το
    #                                                          τελευταίο \n από τη λέξη και τη μετατρέπει σε κεφαλαία
    the_word_with_spaces = " ".join(the_word)  # Βάζει κενά ανάμεσα στη λέξη πχ "Λ Ε Ξ Η"
    lbl_word.set(" ".join("_" * len(the_word)))  # Δημιουργεί μια συμβολοσειρά ίδια σε μήκος με τη λέξη με κενά
    #                                                και αντί για γράμματα έχει κάτω παύλα πχ "_ _ _ _"
    lbl_wrong.set("Λάθος Γράμματα :                   ")  # Δημιουργεί μια συμβολοσειρά για τα λάθος γράμματα


# Συνάρτηση για το τι γίνεται όταν πατιέται ένα γράμμα
def guess(letter):
    global the_word
    global number_of_guesses
    txt = list(the_word_with_spaces)  # Ορίζουμε μια λίστα με όλα τα γράμματα της λέξης που ψάχνουμε
    guessed = list(lbl_word.get())  # Ορίζουμε μια λίστα με όλα τα γράμματα που έχουν βρεθεί μέχρι στιγμής
    wrong = list(lbl_wrong.get())  # Ορίζουμε μια λίστα για τα λάθος γράμματα
    btn[letter_value(letter)].config(state=DISABLED)  # Απενεργοποιεί το κουμπί που πατήθηκε
    if the_word_with_spaces.count(letter) > 0:  # Αν το γράμμα που πατήθηκε βρίσκεται τουλάχιστον 1 φορά στη λέξη
        for _ in range(len(txt)):  # Επανάληψη όσες φορές είναι το μήκος της λέξης μαζί με τα κενά
            if txt[_] == letter:  # Αν βρεθεί το γράμμα στην επανάληψη
                guessed[_] = letter  # βάζουμε το γράμμα που βρέθηκε στην αντίστοιχη θέση στη λίστα
            lbl_word.set("".join(guessed))  # Ενημερώνουμε το label με το καινούριο γράμμα που βρέθηκε
        if lbl_word.get() == the_word_with_spaces:  # Εάν η ενημερωμένη λίστα είναι ίδια με τη λέξη που ψάχνουμε
            msg.showinfo("ΚΡΕΜΑΛΑ", "Συγχαρητήρια!\nΚέρδισες")  # μήνυμα ότι βρέθηκε
            keyboard_active(False)  # Απενεργοποίηση κουμπιών αλφαβήτου
    else:  # Εάν το γράμμα που πατήσαμε δεν είναι στη λέξη
        number_of_guesses += 1  # Αυξάνει τον αριθμό των λάθος μαντεψιών
        img_label.config(image=images[9 - max_number_of_guesses + number_of_guesses])  # Αλλάζει την εικόνα της κρεμάλας
        wrong[15 + 2 * number_of_guesses] = letter  # Ενημερώνει τη λίστα με τα λάθος γράμματα
        lbl_wrong.set("".join(wrong))  # Ενημερώνει το label
        if number_of_guesses == max_number_of_guesses:  # Αν σε αυτό το σημείο φτάσουμε στα μέγιστα λάθη
            msg.showwarning("ΚΡΕΜΑΛΑ", "GAME OVER!\nΗ σωστή λέξη είναι: " + str(the_word))  # Μήνυμα Game Over
            keyboard_active(False)  # Απενεργοποίηση κουμπιών αλφαβήτου


# Συνάρτηση για ενεργοποίηση / απενεργοποίηση κουμπιών αλφαβήτου
def keyboard_active(active):
    if active:
        for _ in range(len(alphabet)):
            btn[_].config(state=ACTIVE)  # Ενεργοποιεί όλα τα κουμπιά
    else:
        for _ in range(len(alphabet)):
            btn[_].config(state=DISABLED)  # Απενεργοποιεί όλα τα κουμπιά


#  Συνάρτηση για να υπολογίσει το index που έχει το κουμπί από το κάθε γράμμα
def letter_value(letter):
    i = 0  # Αρχικοποίηση της τιμής i που είναι το index
    for _ in alphabet:
        if _ == letter:
            break  # Ελέγχει όλα τα γράμματα της αλφαβήτου μέχρι να βρει το γράμμα που θέλουμε αυξάνοντας παράλληλα
        i += 1  # τον μετρητή και με το που το βρει σπάει η λούπα
    return i  # Επιστέφει την τιμή του index


# Συνάρτηση επιλογής δυσκολίας
def set_difficulty(difficulty):
    global max_number_of_guesses
    global top_window
    max_number_of_guesses = difficulty  # Ορισμός του μέγιστου αριθμού μαντεψιών με βάση τη δυσκολία
    keyboard_active(True)  # Ενεργοποίηση κουμπιών αλφαβήτου
    top_window.destroy()  # Κλείσιμο του παραθύρου επιλογής δυσκολίας
    btn_dif.config(state=ACTIVE)  # Ενεργοποιεί το κουμπί επιλογής δυσκολίας
    game()  # Έναρξη παιχνιδιού


# Συνάρτηση παραθύρου επιλογής δυσκολίας
def set_difficulty_window():
    global top_window
    top_window = Toplevel()  # Δημιουργία παραθύρου
    top_window.title("ΚΡΕΜΑΛΑ: ΕΠΙΛΟΓΗ ΔΥΣΚΟΛΙΑΣ")  # Τίτλος παραθύρου
    top_window.iconbitmap("images/hangman.ico")  # Εικονίδιο παραθύρου
    top_window.resizable(False, False)  # Επιλογή να μην αλλάζει μέγεθος
    text_label = Label(top_window, text="Επιλογή Δυσκολίας: ")  # Απλό κείμενο που εμφανίζεται στο παράθυρο
    text_label.grid(row=1, column=0)  # Θέση του κειμένου
    btn_easy = Button(top_window, text="Εύκολο", command=lambda: set_difficulty(9))  # Δημιουργία κουμπιού
    btn_easy.grid(row=1, column=1)  # Θέση κουμπιού
    btn_medium = Button(top_window, text="Μεσαίο", command=lambda: set_difficulty(8))
    btn_medium.grid(row=1, column=2)
    btn_hard = Button(top_window, text="Δύσκολο", command=lambda: set_difficulty(7))
    btn_hard.grid(row=1, column=3)
    btn_very_hard = Button(top_window, text="Πολύ Δύσκολο", command=lambda: set_difficulty(6))
    btn_very_hard.grid(row=1, column=4)
    btn_dif.config(state=DISABLED)  # Απενεργοποιεί το κουμπί επιλογής δυσκολίας
    keyboard_active(False)  # Απενεργοποίηση κουμπιών αλφαβήτου


# Καθορισμός παράθυρου κρεμάλας
img_label = Label(main_window)  # Ορίζει ένα label στο οποίο θα φαίνεται η εικόνα της κρεμάλας στο παράθυρο
img_label.grid(row=0, column=0, columnspan=3, padx=10, pady=40)  # Θέση της εικόνας
img_label.config(image=images[3])  # Καθορίζει ποια εικόνα να δείχνει αρχικά


# Ορισμός των κουμπιών του Ελληνικού Αλφαβήτου
alphabet = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ",
            "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]  # Λίστα με τα ελληνικά γράμματα
n = 0  # Αρχικοποίηση τιμής για τη for
btn = []  # Ορισμός μιας λίστας που θα αποθηκευτούν τα κουμπιά
for _ in alphabet:  # Λούπα για να φτιαχτούν τα κουμπιά με τα ελληνικά γράμματα στο GUI
    btn.append(Button(main_window, text=_, command=lambda letter=_: guess(letter),
                      font="Helvetica 18", width=4))  # Φτιάχνει τα κουμπιά
    btn[n].grid(row=4 + n // 8, column=n % 8)  # Καθορίζει τη θέση κάθε κουμπιού
    btn[n].config(state=DISABLED)  # Θέτει όλα τα κουμπιά απενεργοποιημένα
    n += 1  # Αυξάνει το μετρητή

# Κουμπί για νέο παιχνίδι
Button(main_window, text="Νέο\nΠαιχνίδι", command=lambda: game(),
       font="Helvetica 10 bold").grid(row=4, column=8)

# Κουμπί επιλογής δυσκολίας
btn_dif = Button(main_window, text="Επίπεδο\nΔυσκολίας", command=lambda: set_difficulty_window(),
                 font="Helvetica 10 bold")  # Ορισμός
btn_dif.grid(row=5, column=8)  # Θέση
btn_dif.config(state=ACTIVE)  # Ενεργοποίηση

# Κουμπί Εξόδου από το πρόγραμμα
Button(main_window, text="Έξοδος", command=main_window.quit,
       font="Helvetica 10 bold").grid(row=6, column=8)

# Καθορισμός του που να φαίνεται η άγνωστη λέξη στο παράθυρο
lbl_word = StringVar()
Label(main_window, textvariable=lbl_word, font="Consolas 24 bold").grid(row=0, column=3, columnspan=6, padx=1)

# Καθορισμός για το που να βγαίνουν τα λάθος γράμματα
lbl_wrong = StringVar()
Label(main_window, textvariable=lbl_wrong, font="Consolas 20 bold").grid(row=1, column=1, columnspan=6, padx=1)

# Κλήση της συνάρτησης για να ξεκινήσει το παιχνίδι
game()

# Λούπα για να ενημερώνεται συνέχεια το παράθυρο και να παραμένει ανοιχτό
main_window.mainloop()
