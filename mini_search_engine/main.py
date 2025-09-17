from search_module import Search

app = Search()
if __name__ == '__main__':
    doc = app.load_documents('mini_search_engine\data')
    index, doc_length = app.build_index(doc)

    while True:
        query = input('search query or (q to exit) ')
        if query.lower() == 'q':
            break
        result = app.search(query, doc, index, doc_length)
        if result:
            print('result:')
            for name, score in result:
                print(f'{name}          (score={score:.4f})')
        else: print('no result')