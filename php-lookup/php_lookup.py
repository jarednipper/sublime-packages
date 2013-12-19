import sublime, sublime_plugin
import webbrowser

class PhpLookupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            sel_txt = self.view.substr(sel).strip()
            if sel_txt == '': continue
            doc_url = 'http://php.net/' + sel_txt
            webbrowser.open_new_tab(doc_url)
