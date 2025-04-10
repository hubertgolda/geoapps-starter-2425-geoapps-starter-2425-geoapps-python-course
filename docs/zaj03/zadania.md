Dodaj następujące funkcjonalności do programu przedstawionego jako przykład. Dla wszystkich dodanych funkcjonalności stwórz przykładowy kod potwierdzający, że działają (rozbudowując kod w `main_zajecia03.py`).

1. Zmodyfikuj każdą klasę tak, żeby posiadała atrybut `__max_id`, który będzie wykorzystywany do nadawania identyfikatorów kolejnym stworzonym instancjom (zamiast podawania go jako argument przy inicjalizacji).

2. Rozbuduj klasę `Incident` o priorytet zdarzenia, czas zgłoszenia i informacje o zgłaszającym.

3. Zaprojektuj w ramach subpakietu `fleet` klasę `Station`, każda stacja ma posiadać identyfikator, lokalizację, karetkę, kierowcę i 1 dodatkowego pracownika. Napisz metodę, która sprawdza czy karetka jest na miejscu (czy zgadzają się lokalizacje).

4. Rozbuduj aplikację (w tym zaprojektuj logikę, ale także elementy, które trzeba dodać w różnych klasach (niekoniecznie istniejących) o możliwość zarządzania incydentami – przydzielanie karetek do zgłaszanych zdarzeń. Te funkcjonalności muszą uwzględniać:

    - Priorytet i czas, który upłynął od zgłoszenia,
    - Aktualny stan, w którym znajduje się karetka,
    - Odległość karetki od zdarzenia.