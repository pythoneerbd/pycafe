{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "480a0806",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your value: 19\n",
      "Finished\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Enter your value: \"))\n",
    "if x < 10:\n",
    "    print(\"smaller\")\n",
    "if x > 20:\n",
    "    print(\"Bigger\")\n",
    "print(\"Finished\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8d2c2c73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you can admit aiub\n"
     ]
    }
   ],
   "source": [
    "rating = 4\n",
    "brac = 5\n",
    "east_west = 3\n",
    "aiub = 4\n",
    "\n",
    "if brac == rating :\n",
    "    print(\"you can admit brac\")\n",
    "elif east_west == rating:\n",
    "    print(\"you can admit East West\")\n",
    "elif aiub == rating:\n",
    "    print(\"you can admit aiub\")\n",
    "else:\n",
    "    print(\"Search better option\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "22bf3746",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you can admit east west\n"
     ]
    }
   ],
   "source": [
    "budget = 7\n",
    "brac = 10\n",
    "east_west = 6\n",
    "aiub = 8\n",
    "\n",
    "if budget >= brac:\n",
    "    print(\"You can admit brac\")\n",
    "elif budget >= east_west:\n",
    "    print(\"you can admit east west\")\n",
    "elif budget >= aiub:\n",
    "    print(\"you can admit aiub\")\n",
    "else:\n",
    "    print(\"Please increase your budget\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b10f6452",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you can admit east_west\n"
     ]
    }
   ],
   "source": [
    "weaver = 35\n",
    "brac = 30\n",
    "east_west = 40\n",
    "aiub = 35\n",
    "if weaver <= brac:\n",
    "    print(\"you can admit brac\")\n",
    "elif weaver <= east_west:\n",
    "    print(\"you can admit east_west\")\n",
    "elif weaver <= aiub:\n",
    "    print(\"you can admit aiub\")\n",
    "else:\n",
    "    print(\"Please down your weaver expectation\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26f5fc20",
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
