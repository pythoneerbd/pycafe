{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "628d2f2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.\n",
    "\n",
    "Enter Hours: 45\n",
    "Enter Rate: 10\n",
    "Pay: 475.0'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dc2f1fdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your working hour: 45\n",
      "475.0\n"
     ]
    }
   ],
   "source": [
    "hour = int(input(\"Enter your working hour: \"))\n",
    "rate = 10\n",
    "pay = 0\n",
    "\n",
    "if hour > 40:\n",
    "    pay = (hour-40)*1.5*rate+(rate*40)\n",
    "else:\n",
    "    pay = hour * rate\n",
    "\n",
    "print(pay)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f0034de",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:\n",
    "\n",
    "Enter Hours: 20\n",
    "Enter Rate: nine\n",
    "Error, please enter numeric input\n",
    "Enter Hours: forty\n",
    "Error, please enter numeric input'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c76c059",
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    hour = int(input(\"Enter your working hour: \"))\n",
    "    rate = int(input(\"Enter your hourly rate: \"))\n",
    "    pay = hour*rate\n",
    "    print(pay)\n",
    "except:\n",
    "    print(\"Error!! Please enter numaric value!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3d397f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:\n",
    "Score Grade\n",
    ">= 0.9 A\n",
    ">= 0.8. B\n",
    ">= 0.7 C\n",
    ">= 0.6 D\n",
    "< 0.6 F\n",
    "\n",
    "Enter score: 0.95\n",
    "A\n",
    "Enter score: perfect\n",
    "Bad score\n",
    "Enter score: 10.0\n",
    "Bad score\n",
    "Enter score: 0.75\n",
    "C\n",
    "Enter score: 0.5\n",
    "F\n",
    "\n",
    "Run the program repeatedly as shown above to test the various different values for\n",
    "input.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "06e2ee0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter your score: nine\n",
      "Bad Score\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    score = float(input(\"Please enter your score: \"))\n",
    "    if score >= 0.0 and score <= 1.0:\n",
    "        if score >= 0.9:\n",
    "            print(\"A\")\n",
    "        elif score >= 0.8:\n",
    "            print(\"B\")\n",
    "        elif score >= 0.7:\n",
    "            print(\"C\")\n",
    "        elif score >= 0.6:\n",
    "            print(\"D\")\n",
    "        elif score < 0.6:\n",
    "            print(\"F\")\n",
    "    else:\n",
    "        print(\"Bad Score\")\n",
    "except:\n",
    "    print(\"Bad Score\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f951137",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
