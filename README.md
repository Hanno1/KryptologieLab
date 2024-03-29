KryptologieLab Lösungen

Benutzungsanleitung:
Zum Ausführen der Dateien gehe immer in den entsprechenden Unterordner. Bei mir wird python über die Kommandozeile mit `py` ausgeführt.

1. Aufgabe - additive Chiffre:
- Verschlüsselung: Gib `py additive_encript.py <input_file> <key> <output_file>` in die Konsole ein. input_file ist der Name der Input Datei wo dein Originaltext steht, der key ist eine Zahl zwischen 0 und 25 und wird zum Verschlüsseln genutzt. output_file ist das File, wo der verschlüsselte text reingeschrieben wird. Wenn die Datei bereits existiert, so wird der Inhalt überschrieben.
- Entschlüsselung: Gib `py additive_decrypt.py <input_file> <key> <output_file>` in die Konsole ein. input_file ist nun das File mit dem verschlüsselten Text, key ist der Key, der zum Entschlüsseln genutzt wird. Es ist wieder eine Zahl zwischen 0 und 25. Der enstandene Klartext wird in output_file geschrieben.
- Brechen: Gibt `py additive_break.py <input_file> <output_file>` in die Konsole ein. `<input_file>` ist das File, wo der verschlüsselte Text steht. Der Text sollte nicht zu kurz sein, da das Brechen der Chiffre auf einer Häufigkeitsanalyse basiert. In das gegebene output_file wird zunächst der key geschrieben, der vermutlich zum verschlüsseln genutzt wird. Anschließend wird der verschlüsselte Kryptotext in den nächsten Zeilen dazugeschrieben.

2. Aufgabe - vigenere Chiffre
- Verschlüsselung: Gib `py vigenere_encrypt.py <input_file> <keys> <output_file>` in die Konsole ein. input_file ist der Originaltext. output_file: dort wird der verschlüsselte Text reingeschrieben. keys ist nun ein String mit Buchstaben zwischen A und Z, bspw keys = `ABBFG`.
- Entschlüsselung: War keine Aufgabe, aber ist ganz praktisch zum Testen. Gib `py vigener_decrypt.py <input_file> <keys> <output_file>` in die Konsole ein. 
- Brechen: Gibt `py vigenere_break.py <input_file> <output_file>` in die Konsole ein. Alles funktioniert im Prinzip wie bei der additiven Chiffre, nur das der key aus einem oder mehreren Buchstaben besteht. Der key wird analog wie bei der additiven Chiffre in die output Datei reingeschrieben.

3. Aufgabe - betriebsmodi und AES. 4.te Aufgabe und 5.te Aufgabe wurde auch beide im Ordner 03 erledigt. Zum Ausführen von Aufgabe 3,4 oder 5, gehe immer in den Ordner 03
- Es sind 4 Betriebsmodi implementiert: ecb, cbc, ofb und ctr. Sie sind in den files krypto_ecb_main.py, krypto_cbc_main.py, krypto_ofb_main.py und krypto_ctr_main.py implementiert.

4. Aufgabe - AES
- Verschlüsselung: Gib `py aes_encrypt.py <input_file> <key_file> <output_file>` in die Konsole ein. input_file enthält den Originaltext als hex Folge kodiert. key_file enthält 11 Rundenschüssel, ebenfalls als hex Folge. Das Resultat der Verschlüsselung wird in output_file geschrieben. Ebenfalls als hex Folge. Die Input Datei muss genau 128 Bit enthalten, also 32 Hexzahlen (32*4 = 128).
- Entschlüsselung: Gib `py aes_decrypt.py <input_file> <key_file> <output_file>` in die Konsole ein. Der Inhalt der Dateien muss hexadezimal sein. Auch hier muss der Input 32 Hexzahlen enthalten.

5. Aufgabe - AES Keygen und Kombinierung AES, Betriebsmodi
- Die Schlüssel im AES werden meist nicht einzeln gegeben sondern, es wird lediglich ein 128 Bit langer Schlüssel gegeben und die anderen 10 Schlüssel werden darauf berechnet. Dafür ist die Datei aes_keygen.py da. Ab jetzt sind in der Schlüsseldatei nur noch 128 Bit, also 32 Hex Zahlen. Da es keine Aufgabe war, die Schlüsselgenerierung extra als aufrufbare Datei zu implementieren, wurde das auch nicht gemacht.
- Nun wurde der AES mit den Betriebsmodis kombiniert. Es gibt jeweils ein Ent- und ein Verschlüsselungsprogramm. 
- Verschlüsselung: Gib `py betriebsmodi_encrypt.py <bm> <input_file> <key_file> <output_file> <iv>` in die Konsole ein. bm ist der Betriebsmodi, der verwendet werden soll. Es ist entweder ecb, cbc, ofb oder ctr. Groß- bzw. Kleinschreibung ist egal. input_file enthält den Orignaltext als hexfolge. Er kann jetzt beliebig lang werden und ist nicht auf 128 Bit beschränkt. key_file enthält 32 hexzahlen. Die Verschlüsselung wird als hex folge in die output datei geschrieben. Ist der Betriebsmodi cbc oder ofb, so kann noch ein Initialisierungsvektorfile mitgegeben werden. Die Datei enthält ebenfalls 32 Hex.
- Entschlüsselung: Gib `py betriebsmodi_decrypt.py <bm> <input_file> <key_file> <output_file> <iv>` in die Konsole ein.

6. Aufgabe - Lineare Kryptoanalyse
- Verschlüsselung: Gib `py spn_encrypt.py <input_file> <key_file> <output_file>` in die Konsole ein. Alle Dateien sind im Hex Format gespeichert. Der key hat 16 bits, also 4 Hex. 
- Brechen: Gib `py spn_break.py <orignal_text> <encryptet_text>` in die Konsole ein. Der Algorithmus wird den 2.ten und 4.ten Teilschlüssel in der Konsole ausgeben. Umso mehr Klartext- Kryptotextpaare übergeben werden, umso wahrscheinlicher wird der Schlüssel korrekt sein. Die Inputs sollten zufällig generiert worden sein und im output file stehen die dazugehörigen verschlüsselten Hexwerte.
- Brechen-analyse: Gib `py spn_break_analyses.py <text_count> <repetitions>` in die Konsole ein. text_count und repetitions sind optional. text_count beschreibt die Anzahl an Klartext-Kryptotextpaaren. Für eine sinnvolle Analyse sollte es mindestens 8000 sein. Für einen aussagekräftigen wert kann das Brechen der Chiffre mit neuen Text und Schlüssel wiederholt werden. Dazu ist der Wert repetitions da. Für 8000 Paare schein die Wahrscheinlichkeit die Teilschlüssel korrekt zu bekommen, etwa 60-80%. Das Analyseergebnis für 10 Wiederholungen und 1_000-12_000 paaren (in 1000 Schritten) ist ![Analyseergebnis](analysis_spn.png).
Die Repetitions scheinen zu niedrig, aber es ist doch zu sehen, dass die Wahrscheinlichkeit bei 8_000 Paaren zwischen 80% und 100% zu sein scheint.

7. Aufgabe - Lineare Approximation: Güte
- Güte Bestimmung der Linearen Approximation einer S-Box: Gib `py spn_get_bias.py <s_box_file> <linear_approx_file>` in die Konsole ein. Linear Approximation Datei ist eine Datei, wo die lineare Approximation drin kodiert ist. Diese Approximation wird auch zuächst getestet. Das s_box_file enthält die SBox für die Lineare Kryptoanalyse. Beim Ausführen wird der Bias dieser Approximation in der Konsole ausgegeben. Ist er -1, so ist die Approximation für die S-Box und die Permutation nicht korrekt. Ansonsten sollte ein positiver Wert rauskommen. Umso kleiner der bias, umso besser die Approximation.

8. Aufgabe - RSA 
- Implementierung des RSA-Algorithmus. Zum Ausführen gehe in das verzeichnis `08_RSA` und gib in die Kommandozeile `py rsa.py <input_file> <key_file> <output_file>`. Das <input_file> enthält genau eine Dezimalzahl, die kodiert bzw dekodiert werden soll. Das <keyfile> enthält zwei Zeile: Die erste Zeile ist der Schlüssel zum kodieren bzw. dekodieren (e bzw. d) und die zweite Zeile enthält das n. Das Resultat der Kodierung bzw. Dekodierung wird in das angegbene <output_file> geschrieben.

9. Aufgabe - RSA Schlüsselgenerierung
- Die 9.te Aufgabe ist sinnvollerweise ebenfalls im 08_RSA Ordner, um die Ergebnisse der Schlüsselgenerierung gleich testen zu können. Zum Ausführen muss `py rsa_keygen.py <length> <private_key> <open_key> <prime_numbers>` in die Konsole eingegeben werden. <lenght> beschreibt die gewünschte Schlüssellänge. Es ist sinnvoll eine Länge von etwa 1000 zu wählen. Dann werden die beiden Schlüssel berechnet. Anschließend werden die Schlüssel gespeichert: Der private Schlüssel kommt in das File <private_key> und der öffentliche in <open_key>. In die zweite Zeile der Schlüsselfiles wird das n gespeichert - also das Produkt der genutzten Primzahlen. Zur Kontrolle werden die verwendeten, zufälligen Primzahlen im file <prime_numbers> gespeichert.

10. Aufgabe - Diffie Hellmann Schlüsselaustausch
- Die 10.te Aufgabe befindet sich im Ordner 10_diffie_helmann. Zum Ausführen muss `py diffie_hellman.py <bitlength>` in die Konsole eingegeben werden. Die Variable <bitlength> beschreibt die Länge der verwendeten Primzahlen (circa). Diese Zahl sollte nicht zu groß werden. Eine Größe von etwa 100 sollte ausreichen. Die Ausgabe ist in der Konsole und beinhaltet die Primzahl p, den Generator g, Alices Berechnung A, Bobs Berechnung B und das gemeinsame Geheimnis S.

11. Aufgabe - Sha3 224
- Die 11.te Aufgabe ist im Ordner 11:SHA gespeichert. Zum Ausführen muss `py sha3.py <input_file> <output_file>` in die Konsole eingegeben werden. <input_file> ist die Datei, in der der zu hashende Text steht. Der Text ist im hexadezimal Format gespeichert. Das Resultat des Hashing wir in das file <output_file> geschrieben. Das Format ist ebenfalls hexadezimal. Es wurde mit dem Text "Hello World" getestet und das Ergebnis stimmt nach dem online Hashalgorithmus [hier](https://emn178.github.io/online-tools/sha3_224.html).
