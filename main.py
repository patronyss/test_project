import tkinter as tk
import datebase
import parse


class Root:
    def __init__(self):
        self.db = datebase.DateBase()
        self.parser = parse.Parser()
        self.active_roots = []
        self.run()

    def run(self):
        root = tk.Tk()
        root.title('The ultimate parser')
        root.geometry('800x600')
        root.resizable(False, False)
        self.active_roots.append('Main')

        add_site_btn = tk.Button(root,
                                 text='Додати сайт',
                                 command=self.add_site)
        search_btn = tk.Button(root,
                               text='Знайти інформацію',
                               command=self.search)
        clear_db_btn = tk.Button(root,
                                 text='Очистити БД',
                                 command=self.clear_db)
        print_db_btn = tk.Button(root,
                                 text='Список сайтів',
                                 command=self.print_db)

        add_site_btn.pack()
        search_btn.pack()
        clear_db_btn.pack()
        print_db_btn.pack()

        root.mainloop()

    def clear_db(self):
        self.db.clear_db()

    def search(self):
        def delete():
            self.active_roots.remove('Search')
            search_root.destroy()

        def start():
            info = search_entry.get()
            sites_names = self._get_sites_names(self.db.get_sites())
            res = dict()
            for site in sites_names:
                res[site] = self.parser.parse_count_of_info(site, info)
            res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
            search_entry.destroy()
            search_button.destroy()
            text = ''
            count = 1
            for key, value in res.items():
                text += f'{count}. {key} : {value} \n'
                count += 1

            result_label.config(text=text)
            result_label.pack()


        if 'Search' not in self.active_roots:
            search_root = tk.Tk()
            search_root.title('Пошук')
            search_root.attributes("-topmost", True)
            self.active_roots.append('Search')
            search_root.protocol('WM_DELETE_WINDOW', delete)

            search_entry = tk.Entry(search_root)
            search_button = tk.Button(search_root,
                                      text='SEARCH',
                                      command=start)
            result_label = tk.Label(search_root)

            search_entry.pack()
            search_button.pack()

            search_root.mainloop()

    def add_site(self):
        def delete():
            self.active_roots.remove('Add_site')
            add_root.destroy()

        def start():
            info = site_entry.get()
            if self.parser.true_response(info):
                self.db.add_site(info)

        if 'Add_site' not in self.active_roots:
            add_root = tk.Tk()
            add_root.title('Додати сайт')
            self.active_roots.append('Add_site')
            add_root.protocol('WM_DELETE_WINDOW', delete)

            add_btn = tk.Button(add_root,
                                text='Додати сайт до БД',
                                command=start)
            site_entry = tk.Entry(add_root)

            site_entry.pack()
            add_btn.pack()

            add_root.mainloop()

    def print_db(self):
        def delete():
            self.active_roots.remove('print_db')
            print_root.destroy()

        if 'print_db' not in self.active_roots:
            self.active_roots.append('print_db')
            print_root = tk.Tk()
            print_root.protocol('WM_DELETE_WINDOW', delete)

            sites_names = self._get_sites_names(self.db.get_sites())
            text = self._create_sites_list(sites_names)

            label = tk.Label(print_root,
                             text=text)

            label.pack()

            print_root.mainloop()

    def _get_sites_names(self, db_info: list):
        return [el[1] for el in db_info]

    def _create_sites_list(self, sites_names: list):
        text = ''
        count = 1
        for el in sites_names:
            text += f'{count} - {el} \n'
            count += 1
        return text


if __name__ == '__main__':
    Root()
