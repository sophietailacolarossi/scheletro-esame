import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        lista=self._model.returnDD()
        listaDD = [ft.dropdown.Option(text= l, key=l) for l in lista]
        self._view._dd.options = listaDD
        self._view._dd.options = listaDD
        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()

        valore = self._view._dd.value

        if valore is None:
            self._view.create_alert("Selezionare un valore dal dropdown.")
            return

        try:
            self._model.buildGraph(valore)

            self._view._txt_result.controls.append(
                ft.Text("Grafo correttamente creato.")
            )
            self._view._txt_result.controls.append(
                ft.Text(f"Numero nodi: {self._model.getNumNodi()}")
            )
            self._view._txt_result.controls.append(
                ft.Text(f"Numero archi: {self._model.getNumArchi()}")
            )

            self._view.update_page()

        except Exception as ex:
            self._view.create_alert(f"Errore nella creazione del grafo: {ex}")

        self._view.update_page()

    def handleStampaInfo(self, e):
        self._view._txt_result.controls.clear()

        if self._model.getNumNodi() == 0:
            self._view.create_alert("Creare prima il grafo.")
            return

        try:
            dettagli1 = self._model.stampaDettagli1()
            if dettagli1:
                self._view._txt_result.controls.append(
                    ft.Text(f"Dettagli1: {dettagli1}")
                )
            else:
                self._view._txt_result.controls.append(
                    ft.Text("Attenzione!...")
                )

            dettagli2 = self._model.stampaDettagli2()
            if dettagli2:
                self._view._txt_result.controls.append(
                    ft.Text(f"{dettagli2}")
                )
                for i, (u, v, weight) in enumerate(dettagli1, 1):
                    self._view._txt_result.controls.append(
                        ft.Text(f"{i}. {u} -> {v} (peso: {weight})")
                    )
            else:
                self._view._txt_result.controls.append(
                    ft.Text("Attenzione!...")
                )

            self._view.update_page()

        except Exception as ex:
            self._view.create_alert(f"Errore nella stampa delle info: {ex}")

    def handleCammino(self, e):
        self._view._txt_result.controls.clear()

        if self._model.getNumNodi() == 0:
            self._view.create_alert("Creare prima il grafo.")
            return

        if self._view._valore is None:
            self._view.create_alert("Selezionare un cliente.")
            return

        try:
            sequence_result = self._model.handleRicorsione(self._view._valore)

            if sequence_result is None or len(sequence_result) == 0:
                self._view._txt_result.controls.append(
                    ft.Text("Nessuna sequenza trovata.")
                )
                self._view.update_page()
                return

            path, score = sequence_result

            self._view._txt_result.controls.append(
                ft.Text("Sequenza trovata:")
            )
            self._view._txt_result.controls.append(ft.Text(""))

            for node in path:
                self._view._txt_result.controls.append(
                    ft.Text(f"Dettaglio: {node}")
                )

            self._view._txt_result.controls.append(ft.Text(""))
            self._view._txt_result.controls.append(
                ft.Text(f"Numero archi nel percorso: {len(path) - 1}")
            )
            self._view._txt_result.controls.append(
                ft.Text(f"Punteggio: {score}")
            )

            self._view.update_page()

        except Exception as ex:
            self._view.create_alert(f"Errore nella ricerca della sequenza: {ex}")