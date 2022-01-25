{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9957f50a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3a373cb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "print(type(2.2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "add7d78d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'complex'>\n"
     ]
    }
   ],
   "source": [
    "print(type(complex(2,3)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ab6ead12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "print('Hello world')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9ad11168",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print(type('hello world'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f06a9141",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print(type(\"Today's new paper\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4afbb0ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "val1 = 2\n",
    "val2 = 3\n",
    "res = val1 + val2\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7b3f0090",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1\n"
     ]
    }
   ],
   "source": [
    "val1 = 2\n",
    "val2 = 3\n",
    "res = val1 - val2\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b1d02c21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "val1 = 2\n",
    "val2 = 3\n",
    "res = val1 * val2\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "67badf53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n"
     ]
    }
   ],
   "source": [
    "val1 = 10 \n",
    "val2 = 2\n",
    "res = val1 / val2\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "87a47ef6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "val1 = 3\n",
    "val2 = 2\n",
    "res = val1 % val2\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5516878b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "val1 = 2\n",
    "val2 = 3\n",
    "res = val1 ** val2\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "421a4961",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "val1 = 3\n",
    "val2 = 2\n",
    "res = val1 // val2\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "381782bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "namenabir\n"
     ]
    }
   ],
   "source": [
    "a = \"name\"\n",
    "b = \"nabir\"\n",
    "print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d14e9cb4",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'Please enter your first value: '",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_8132/546405720.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mval1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Please enter your first value: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mval2\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Please enter your second value: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mres\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mval1\u001b[0m \u001b[1;33m/\u001b[0m \u001b[0mval2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mres\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'Please enter your first value: '"
     ]
    }
   ],
   "source": [
    "val1 = input(int(\"Please enter your first value: \"))\n",
    "val2 = input(int(\"Please enter your second value: \"))\n",
    "res = val1 / val2\n",
    "print(res)"
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
