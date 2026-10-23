# Panduan Ekspor BibTeX

Untuk alur kerja I. Membuat entri BibTeX dari metadata OpenAlex atau Crossref, agar bisa dipakai di Zotero, Overleaf, dan Mendeley.

## Padanan jenis entri

- Artikel jurnal: `@article`, wajib `author, title, journal, year, volume, number, pages, doi`.
- Artikel konferensi: `@inproceedings`, wajib `author, title, booktitle, year, pages, doi`.
- Buku: `@book`, wajib `author` atau `editor, title, publisher, year`.
- Tesis: `@phdthesis` atau `@mastersthesis`, wajib `author, title, school, year`.
- Preprint: `@misc`, wajib `author, title, year, eprint` berisi arXiv ID, dan `archivePrefix="arXiv"`.
- Halaman web: `@misc`, wajib `author, title, year, howpublished="\url{...}"`, dan `note` berisi tanggal akses.

## Aturan pembuatan

- Field penulis disambung dengan `and`, memakai bentuk "Nama belakang, Nama depan" karena paling stabil di BibTeX. Penulis Indonesia ditulis nama lengkap, dan bila nama tunggal dipakai, apit dengan kurung kurawal.
- Judul mempertahankan huruf aslinya. Kata yang mudah diubah LaTeX menjadi huruf kecil, misalnya IEEE, GPT, RAG, dibungkus kurung kurawal: `title = {A Survey on {RAG}}`.
- DOI ditulis di field `doi` tanpa awalan URL.
- Key dibuat dari nama belakang penulis pertama, tahun, dan kata pertama judul, misalnya `vaswani2017attention`, dan tidak boleh sama dalam satu berkas bib.
- Utamakan `family` dan `given` dari Crossref. `display_name` OpenAlex tidak punya batas nama yang andal, jadi jangan memakai `rsplit` untuk menebak nama majemuk atau aturan penamaan budaya. Bila hanya ada `display_name`, simpan nama apa adanya dan tandai perlu diperiksa, jangan diurutkan ulang diam-diam.
- Kelengkapan field bergantung pada jenis entri dan gaya sitasi; daftar di atas adalah bahan yang dikumpulkan, bukan kewajiban semua gaya. `primary_location` dan `source` di OpenAlex bisa bernilai null, jadi akses berantai dengan `(w.get('primary_location') or {}).get('source') or {}`. Daftar penulis bisa terpotong, jadi cocokkan dengan teks aslinya.
- Contoh berikut memakai metadata Crossref terstruktur. Pada pemakaian nyata, ganti fixture dengan data sebenarnya; field yang tidak diketahui ditandai belum diverifikasi, tidak diisi tahun atau jurnal karangan:

```python
def tex_escape(text):
    replacements = {'\\': r'\textbackslash', '{': r'\{', '}': r'\}',
                    '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
                    '_': r'\_', '~': r'\textasciitilde', '^': r'\textasciicircum'}
    return ''.join(replacements.get(c, c) for c in str(text))

def bibtex_name(author):
    family, given = author.get('family'), author.get('given')
    if family:
        return tex_escape(family) + (', ' + tex_escape(given) if given else '')
    literal = author.get('name') or author.get('display_name')
    if not literal:
        raise ValueError('nama penulis tidak ada; jangan dikarang')
    return '{' + tex_escape(literal) + '}'

authors = [{'family': 'LeCun', 'given': 'Yann'},
           {'family': 'de la Cruz', 'given': 'María'}, {'name': 'Research & Co.'}]
author_field = ' and '.join(map(bibtex_name, authors))
assert bibtex_name(authors[0]) == 'LeCun, Yann'
assert bibtex_name(authors[1]) == 'de la Cruz, María'
assert bibtex_name({'display_name': 'Budi Santoso'}) == '{Budi Santoso}'
assert tex_escape('A_{B} & 5%') == r'A\_\{B\} \& 5\%'
title = tex_escape('Example {RAG} & Methods')
entry = '@misc{example,\n  author = {' + author_field + '},\n  title = {{' + title + '}}\n}'
print(entry)
```

## Literatur Indonesia

Untuk penulisan berbahasa Indonesia, gunakan gaya `biblatex` dengan paket `biblatex-gb7714-2015` hanya bila jurnal memintanya. Untuk jurnal Indonesia pada umumnya, gaya APA 7 lebih lazim dan sudah didukung `biblatex-apa`. BibTeX biasa lemah menangani urutan nama Indonesia dan kata "dkk" atau "et al.", jadi periksa hasilnya secara manual. Entri jurnal Indonesia memakai field yang sama dengan entri berbahasa Inggris.

## Verifikasi

Berkas .bib yang dihasilkan wajib melewati `biber --tool` atau kompilasi Overleaf. Untuk pembuatan massal, periksa tiga entri secara acak dan cocokkan field per field dengan metadata aslinya.
