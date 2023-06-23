    def get_template(self) -> str:
        if self.path.startswith(EVENTS):
            try:
                query = self.get_query(EVENTS_ALL_ATTRS)
            except Exception as error:
                return BAD_REQUEST, str(error)

            return OK, events(get_data(query, EVENTS[1:]))
        elif self.path.startswith(PLACES):
            try:
                query = self.get_query()
            except Exception as error:
                return BAD_REQUEST, str(error)

            return OK, places(get_place(query))
        return OK, main_page()