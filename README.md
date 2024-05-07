## Time Machine ⌚  (IT Documentation)

### Indice

1. [Introduzione](#introduzione)
2. [Descrizione del Progetto](#descrizione-del-progetto)
3. [Struttura dei File](#struttura-dei-file)
4. [Dipendenze](#dipendenze)
5. [Punti di Accesso](#punti-di-accesso)
6. [Come Eseguire](#come-eseguire)

---

### Introduzione

Questo documento fornisce una documentazione completa per il progetto "La Macchina del Tempo", un'applicazione web Flask che consente agli utenti di accedere alle pagine web archiviate dalla Wayback Machine. L'applicazione fornisce un'interfaccia per inserire gli URL e selezionare un anno specifico per visualizzare le versioni archiviate delle pagine web.

### Descrizione del Progetto

Il progetto consiste in un'applicazione web Flask che utilizza l'API CDX della Wayback Machine per recuperare le versioni archiviate delle pagine web in base all'input dell'utente. L'applicazione consente agli utenti di inserire un URL e selezionare un anno specifico, quindi visualizza la versione archiviata della pagina web di quell'anno.

### Struttura dei File

- **main.py**: Applicazione Flask contenente la logica lato server e le definizioni dei punti di accesso.
- **template/whitespace.html**: File template HTML per l'interfaccia web.
- **static/ProductSans-Black.ttf**: File del font per l'interfaccia web.
- **static/ProductSans-Light.ttf**: File del font per l'interfaccia web.

### Dipendenze

Il progetto dipende dalle seguenti librerie Python:

- **Flask**: Framework web per la costruzione dell'applicazione.
- **waybackpy**: Wrapper Python per l'API CDX della Wayback Machine.

### Punti di Accesso

- **/**: Pagina iniziale, visualizza l'interfaccia principale dell'applicazione.
- **/web**: Punto di accesso per recuperare le pagine web archiviate in base all'input dell'utente (URL).
- **/set**: Punto di accesso per impostare l'anno per il recupero delle pagine web archiviate.

### Come Eseguire

Per eseguire l'applicazione:

1. Installare le dipendenze richieste usando `pip install -r requirements.txt`.
2. Eseguire l'applicazione Flask usando `python3 main.py`.
3. Accedere all'applicazione in un browser web all'indirizzo `http://localhost:5000`.

---
