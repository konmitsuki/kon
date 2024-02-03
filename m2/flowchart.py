import pyflowchart as pfc
import nbformat

# # Jupyter Notebook ファイルを開く
# notebook_path = 'C:\\Users\\flow\\Desktop\\konprogram\\m2\\VideoBubbleAnalyzer.ipynb'
# with open(notebook_path, encoding='utf-8') as f:
#     nb = nbformat.read(f, as_version=4)
    
# # コードセルの内容を結合
# code_cells = [cell.source for cell in nb.cells if cell.cell_type == 'code']
# combined_code = "\n".join(code_cells)

# # フローチャートを生成
# fc = pfc.Flowchart.from_code(combined_code)

# with open('C:\\Users\\flow\\Desktop\\master_thesis_data\\flowchart_output.txt', 'w', encoding='utf-8') as out_file:
#     out_file.write(fc.flowchart())

# # print(fc.flowchart())

def generate_flowchart_from_notebook(notebook_path, output_path):
    # Jupyter Notebook ファイルを開く
    with open(notebook_path, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # コードセルの内容を結合
    code_cells = [cell.source for cell in nb.cells if cell.cell_type == 'code']
    combined_code = "\n".join(code_cells)

    # フローチャートを生成
    fc = pfc.Flowchart.from_code(combined_code)

    # フローチャートをファイルに保存
    with open(output_path, 'w', encoding='utf-8') as out_file:
        out_file.write(fc.flowchart())
    
    
# この関数を使用する例
notebook_path = 'C:\\Users\\flow\\Desktop\\konprogram\\m2\\VideoBubbleAnalyzer.ipynb'
output_path = 'C:\\Users\\flow\\Desktop\\master_thesis_data\\flowchart_output.txt'
generate_flowchart_from_notebook(notebook_path, output_path)