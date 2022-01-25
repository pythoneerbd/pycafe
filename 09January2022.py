{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ecb4b1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 8\n",
      "Odd number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "if num % 7 == 0:\n",
    "    print(\"Even number\")\n",
    "else:\n",
    "    print(\"Odd number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "51371d41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your bill unit: 101\n",
      "Your billing amount is:  5\n"
     ]
    }
   ],
   "source": [
    "unit = int(input(\"Enter your bill unit: \"))\n",
    "amount = 0\n",
    "if unit <= 100:\n",
    "    amount = 0\n",
    "elif unit > 100 and unit <= 200:\n",
    "    amount = (unit-100)*5\n",
    "elif unit > 200:\n",
    "    amount = 500+(unit-200)*10\n",
    "else:\n",
    "    print(\"Wrong input\")\n",
    "print(\"Your billing amount is: \", amount)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ee923165",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 12345\n",
      "Last number is:  5\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Enter a number: \"))\n",
    "print(\"Last number is: \", number%10)"
   ]
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
