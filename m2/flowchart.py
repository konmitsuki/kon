import pyflowchart as pfc
import nbformat


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
# notebook_path = 'C:\\Users\\flow\\Desktop\\konprogram\\m2\\VideoBubbleAnalyzer.ipynb'
# output_path = 'C:\\Users\\flow\\Desktop\\master_thesis_data\\flowchart_output.txt'
# generate_flowchart_from_notebook(notebook_path, output_path)

def generate_flowchart_from_notebook(notebook_path, output_path, start_cell=None, end_cell=None, start_line=None, end_line=None):
    with open(notebook_path, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # コードセルの範囲を指定して抽出
    code_cells = nb.cells[start_cell-1:end_cell] if start_cell and end_cell else nb.cells
    code_sections = []
    
    for index, cell in enumerate(code_cells):
        if cell.cell_type == 'code':
            # 行番号範囲でコードを抽出
            lines = cell.source.split('\n')
            if start_line and end_line and index + 1 == start_cell:
                # 指定されたセルと行の範囲内のコードを抽出
                lines = lines[start_line-1:end_line]
            code_sections.append('\n'.join(lines))
    
    combined_code = "\n".join(code_sections)
    
    # コードセクションが空かどうかを確認
    if not combined_code.strip():
        raise ValueError("Specified code section is empty. Check the cell and line range.")
    
    # フローチャートを生成
    fc = pfc.Flowchart.from_code(combined_code)
    print(fc.flowchart())
    
    # フローチャートをファイルに保存
    with open(output_path, 'w', encoding='utf-8') as out_file:
        out_file.write(fc.flowchart())
                
notebook_path = 'C:\\Users\\flow\\Desktop\\konprogram\\m2\\VideoBubbleAnalyzer.ipynb'
output_path = 'C:\\Users\\flow\\Desktop\\master_thesis_data\\flowchart_output.txt'
generate_flowchart_from_notebook(notebook_path, output_path, start_cell=2, end_cell=2, start_line=291, end_line=395)