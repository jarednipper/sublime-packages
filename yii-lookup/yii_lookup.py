import sublime, sublime_plugin
import webbrowser

class YiiLookupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            sel_txt = self.view.substr(sel).strip()
            if sel_txt == '': continue
            doc_url = 'http://www.yiiframework.com/search/?q=' + sel_txt
            webbrowser.open_new_tab(doc_url)
