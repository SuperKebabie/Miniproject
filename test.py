from tkinter import *


def clicked():
    label["text"] = entry.get()


def onclick():
    pass


root = Tk()

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

button = Button(master=root, text='Vertrektijden laden', command=clicked)
button.pack(pady=10)

text = Text(root)
text.insert(INSERT, "Dummy tekst " )
split("/n")
text.insert(END, "Op 2 regels")
text.pack()


button = Button(master=root, text='Terug naar Hoofdscherm', command=clicked)
button.pack(pady=10)


root.mainloop()


#LED CODE SAMPLE

# const int red = 11;
# const int green = 10;
# const int blue = 9;
#
# void setup() {
#   pinMode(blue, OUTPUT);
# }
# void loop() {
#   digitalWrite(blue, HIGH);
#   delay(1000);
#   digitalWrite(blue, LOW);
#   delay(1000);
# }
#
# //
# //const int buttonPin = 3;
# //const int red = 11;
# //const int green = 10;
# //const int blue = 9;
# //int counter = 0;
# //
# //void setup() {
# //  pinMode(buttonPin, INPUT);
# //  pinMode(red, OUTPUT);
# //  pinMode(green, OUTPUT);
# //  pinMode(blue, OUTPUT);
# //}
# //
# //void loop() {
# //  int buttonState;
# //  buttonState = digitalRead(buttonPin);
# //
# //  if (buttonState == LOW) {
# //    counter++;
# //    delay(150);
# //  }
# //
# //  else if (counter == 0) {
# //    digitalWrite(red, LOW);
# //    digitalWrite(green, LOW);
# //    digitalWrite(blue, LOW);
# //  }
# //
# //  else if (counter == 1) {
# //    digitalWrite(red, HIGH);
# //    digitalWrite(green, LOW);
# //    digitalWrite(blue, LOW);
# //  }
# //
# //  else if (counter == 2) {
# //    digitalWrite(red, LOW);
# //    digitalWrite(green, HIGH);
# //    digitalWrite(blue, LOW);
# //  }
# //
# //  else if (counter == 3) {
# //    digitalWrite(red, LOW);
# //    digitalWrite(green, LOW);
# //    digitalWrite(blue, HIGH);
# //  }
# //
# //  else {
# //    counter = 0;
# //  }
# //}
