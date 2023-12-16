KryptologieLab Lösungen

Benutzungsanleitung:
Zum Ausführen der Dateien gehe immer in den entsprechenden Unterordner.

1. Aufgabe - additive Chiffre:
- Verschlüsselung: Gib 'py additive_encript.py <input_file> <key> <output_file>' in die Konsole ein. input_file ist der Name der Input Datei wo dein Originaltext steht, der key ist eine Zahl zwischen 0 und 25 und wird zum Verschlüsseln genutzt. output_file ist das File, wo der verschlüsselte text reingeschrieben wird. Wenn die Datei bereits existiert, so wird der Inhalt überschrieben.
- Entschlüsselung: Gib 'py additive_decrypt.py <input_file> <key> <output_file>' in die Konsole ein. input_file ist nun das File mit dem verschlüsselten Text, key ist der Key, der zum Entschlüsseln genutzt wird. Es ist wieder ein Buchstabe zwischen A und Z. Der enstandene Klartext wird in output_file geschrieben.
- Brechen: Gibt 'py additive_break.py <input_file> <output_file>' in die Konsole ein. input_file ist das File, wo der verschlüsselte Text steht. Der Text sollte nicht zu kurz sein, da das Brechen der Chiffre auf einer Häufigkeitsanalyse basiert. In das gegebene output_file wird zunächst der key geschrieben, der vermutlich zum verschlüsseln genutzt wird. Anschließend wird der verschlüsselte Kryptotext in der nächsten Zeile dazugeschrieben.

2. Aufgabe - vigenere Chiffre
- Verschlüsselung: Gib 'py vigenere_encrypt.py <input_file> <keys> <output_file>' in die Konsole ein. input_file ist der Originaltext. output_file: dort wird der verschlüsselte Text reingeschrieben. keys ist nun ein String mit Buchstaben zwischen A und Z, bspw keys = 'ABBFG'.
- Entschlüsselung: War keine Aufgabe, aber ist ganz praktisch zum Testen. Gib 'py vigener_decrypt.py <input_file> <keys> <output_file>' in die Konsole ein. 
- Brechen: Gibt 'py vigenere_break.py <input_file> <output_file>' in die Konsole ein. Alles funktioniert im Prinzip wie bei der additiven Chiffre, nur das der key aus einem oder mehreren Buchstaben besteht. Der key wird analog wie bei der additiven Chiffre in die output Datei reingeschrieben.

3. Aufgabe - betriebsmodi und AES
