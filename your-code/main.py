{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "toc": true
   },
   "source": [
    "<h1>Table of Contents<span class=\"tocSkip\"></span></h1>\n",
    "<div class=\"toc\"><ul class=\"toc-item\"><li><span><a href=\"#Parallelization-Lab\" data-toc-modified-id=\"Parallelization-Lab-1\"><span class=\"toc-item-num\">1&nbsp;&nbsp;</span>Parallelization Lab</a></span><ul class=\"toc-item\"><li><span><a href=\"#Step-1:-Use-the-requests-library-to-retrieve-the-content-from-the-URL-below.\" data-toc-modified-id=\"Step-1:-Use-the-requests-library-to-retrieve-the-content-from-the-URL-below.-1.1\"><span class=\"toc-item-num\">1.1&nbsp;&nbsp;</span>Step 1: Use the requests library to retrieve the content from the URL below.</a></span></li><li><span><a href=\"#Step-2:-Use-BeautifulSoup-to-extract-a-list-of-all-the-unique-links-on-the-page.\" data-toc-modified-id=\"Step-2:-Use-BeautifulSoup-to-extract-a-list-of-all-the-unique-links-on-the-page.-1.2\"><span class=\"toc-item-num\">1.2&nbsp;&nbsp;</span>Step 2: Use BeautifulSoup to extract a list of all the unique links on the page.</a></span></li><li><span><a href=\"#Step-3:-Use-list-comprehensions-with-conditions-to-clean-the-link-list.\" data-toc-modified-id=\"Step-3:-Use-list-comprehensions-with-conditions-to-clean-the-link-list.-1.3\"><span class=\"toc-item-num\">1.3&nbsp;&nbsp;</span>Step 3: Use list comprehensions with conditions to clean the link list.</a></span></li><li><span><a href=\"#Step-4:-Use-the-os-library-to-create-a-folder-called-wikipedia-and-make-that-the-current-working-directory.\" data-toc-modified-id=\"Step-4:-Use-the-os-library-to-create-a-folder-called-wikipedia-and-make-that-the-current-working-directory.-1.4\"><span class=\"toc-item-num\">1.4&nbsp;&nbsp;</span>Step 4: Use the os library to create a folder called <em>wikipedia</em> and make that the current working directory.</a></span></li><li><span><a href=\"#Step-5:-Write-a-function-called-index_page-that-accepts-a-link-and-does-the-following.\" data-toc-modified-id=\"Step-5:-Write-a-function-called-index_page-that-accepts-a-link-and-does-the-following.-1.5\"><span class=\"toc-item-num\">1.5&nbsp;&nbsp;</span>Step 5: Write a function called index_page that accepts a link and does the following.</a></span></li><li><span><a href=\"#Step-6:-Sequentially-loop-through-the-list-of-links,-running-the-index_page-function-each-time.\" data-toc-modified-id=\"Step-6:-Sequentially-loop-through-the-list-of-links,-running-the-index_page-function-each-time.-1.6\"><span class=\"toc-item-num\">1.6&nbsp;&nbsp;</span>Step 6: Sequentially loop through the list of links, running the index_page function each time.</a></span></li><li><span><a href=\"#Step-7:-Perform-the-page-indexing-in-parallel-and-note-the-difference-in-performance.\" data-toc-modified-id=\"Step-7:-Perform-the-page-indexing-in-parallel-and-note-the-difference-in-performance.-1.7\"><span class=\"toc-item-num\">1.7&nbsp;&nbsp;</span>Step 7: Perform the page indexing in parallel and note the difference in performance.</a></span></li></ul></li></ul></div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Parallelization Lab\n",
    "\n",
    "In this lab, you will be leveraging several concepts you have learned to obtain a list of links from a web page and crawl and index the pages referenced by those links - both sequentially and in parallel. Follow the steps below to complete the lab."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Use the requests library to retrieve the content from the URL below.\n",
    "\n",
    "https://en.wikipedia.org/wiki/Data_science"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests as req\n",
    "\n",
    "url = 'https://en.wikipedia.org/wiki/Data_science'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b'<!DOCTYPE html>\\n<html class=\"client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-enabled vector-feature-sticky-header-disabled vector-feature-page-tools-disabled vector-feature-page-tools-pinned-disabled vector-feature-main-menu-pinned-disabled vector-feature-limited-width-enabled vector-feature-limited-width-content-enabled\" lang=\"en\" dir=\"ltr\">\\n<head>\\n<meta charset=\"UTF-8\"/>\\n<title>Data science - Wikipedia</title>\\n<script>document.documentElement.className=\"client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-enabled vector-feature-sticky-header-disabled vector-feature-page-tools-disabled vector-feature-page-tools-pinned-disabled vector-feature-main-menu-pinned-disabled vector-feature-limited-width-enabled vector-feature-limited-width-content-enabled\";(function(){var cookie=document.cookie.match(/('"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html = req.get(url).content\n",
    "\n",
    "html[:1000]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Use BeautifulSoup to extract a list of all the unique links on the page."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find_all('a')[15].attrs['href']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "437"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "links = []\n",
    "\n",
    "for e in soup.find_all('a'):\n",
    "    \n",
    "    if 'href' in e.attrs:\n",
    "        \n",
    "        links.append(e.attrs['href'])\n",
    "\n",
    "len(links)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['#bodyContent',\n",
       " '/wiki/Main_Page',\n",
       " '/wiki/Special:Search',\n",
       " '/w/index.php?title=Special:CreateAccount&returnto=Data+science',\n",
       " '/w/index.php?title=Special:CreateAccount&returnto=Data+science',\n",
       " '/w/index.php?title=Special:UserLogin&returnto=Data+science',\n",
       " '/wiki/Help:Introduction',\n",
       " '/wiki/Special:MyTalk',\n",
       " '/wiki/Special:MyContributions',\n",
       " '/wiki/Main_Page',\n",
       " '/wiki/Wikipedia:Contents',\n",
       " '/wiki/Portal:Current_events',\n",
       " '/wiki/Special:Random',\n",
       " '/wiki/Wikipedia:About',\n",
       " '//en.wikipedia.org/wiki/Wikipedia:Contact_us',\n",
       " 'https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en',\n",
       " '/wiki/Help:Contents',\n",
       " '/wiki/Help:Introduction',\n",
       " '/wiki/Wikipedia:Community_portal',\n",
       " '/wiki/Special:RecentChanges']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "links[:20]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Use list comprehensions with conditions to clean the link list.\n",
    "\n",
    "There are two types of links, absolute and relative. Absolute links have the full URL and begin with http while relative links begin with a forward slash (/) and point to an internal page within the wikipedia.org domain. Clean the respective types of URLs as follows.\n",
    "\n",
    "- Absolute Links: Create a list of these and remove any that contain a percentage sign (%).\n",
    "- Relativel Links: Create a list of these, add the domain to the link so that you have the full URL, and remove any that contain a percentage sign (%).\n",
    "- Combine the list of absolute and relative links and ensure there are no duplicates."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "domain = 'http://wikipedia.org'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "103"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abs_links = []\n",
    "rel_links = []\n",
    "\n",
    "for e in links:\n",
    "    \n",
    "    if 'https' in e:\n",
    "        abs_links.append(e)    \n",
    "        \n",
    "    else:\n",
    "        rel_links.append(e)\n",
    "    \n",
    "len(rel_links)\n",
    "len(abs_links)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "abs_clean = []\n",
    "\n",
    "for e in abs_links:\n",
    "    abs_clean.append(e.split('%')[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "rel_clean = []\n",
    "\n",
    "for e in rel_links:\n",
    "    rel_clean.append(domain+e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "clean_links = abs_clean + rel_clean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "437"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(clean_links)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "clean_links = list(set(clean_links))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "377"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(clean_links)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['http://wikipedia.org/wiki/Committee_on_Data_for_Science_and_Technology',\n",
       " 'http://wikipedia.org/wiki/Data_format_management',\n",
       " 'http://wikipedia.org/wiki/Extract,_load,_transform',\n",
       " 'https://ja.wikipedia.org/wiki/',\n",
       " 'https://eo.wikipedia.org/wiki/Datuma_scienco',\n",
       " 'http://wikipedia.org/wiki/Graphic_design',\n",
       " 'http://wikipedia.org/wiki/Knowledge',\n",
       " 'http://wikipedia.org//en.m.wikipedia.org/w/index.php?title=Data_science&mobileaction=toggle_view_mobile',\n",
       " 'http://wikipedia.org/wiki/Exploration',\n",
       " 'https://flowingdata.com/2009/06/04/rise-of-the-data-scientist/']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clean_links[:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Use the os library to create a folder called *wikipedia* and make that the current working directory."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "archivos=os.path.join('../data', 'accounts.*.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.exists('wikipedia'): \n",
    "    os.makedirs('wikipedia')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Esto sirve para cambiar el directorio de trabajo. La ruta será sin ../ para lo que esté aquí.\n",
    "os.chdir('wikipedia')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Write a function called index_page that accepts a link and does the following.\n",
    "\n",
    "- Tries to request the content of the page referenced by that link.\n",
    "- Slugifies the filename using the `slugify` function from the [python-slugify](https://pypi.org/project/python-slugify/) library and adds a .html file extension.\n",
    "    - If you don't already have the python-slugify library installed, you can pip install it as follows: `$ pip install python-slugify`.\n",
    "    - To import the slugify function, you would do the following: `from slugify import slugify`.\n",
    "    - You can then slugify a link as follows `slugify(link)`.\n",
    "- Creates a file in the wikipedia folder using the slugified filename and writes the contents of the page to the file.\n",
    "- If an exception occurs during the process above, just `pass`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: python-slugify in c:\\users\\elmat\\anaconda3\\lib\\site-packages (5.0.2)\n",
      "Requirement already satisfied: text-unidecode>=1.3 in c:\\users\\elmat\\anaconda3\\lib\\site-packages (from python-slugify) (1.3)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip available: 22.3.1 -> 23.0\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install python-slugify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from slugify import slugify\n",
    "\n",
    "unicode=str()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "def index_page(s):\n",
    "    #import requests as req\n",
    "    #import os\n",
    "    #from bs4 import BeautifulSoup as bs\n",
    "    try:\n",
    "        html2 = req.get(s).text  \n",
    "        archivo = slugify(s)\n",
    "    \n",
    "        with open(archivo, 'w', encoding='utf-8') as file:\n",
    "            file.write(html2) \n",
    "    except:\n",
    "        pass"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6: Sequentially loop through the list of links, running the index_page function each time.\n",
    "\n",
    "Remember to include `%%time` at the beginning of the cell so that it measures the time it takes for the cell to run."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tqdm in c:\\users\\elmat\\anaconda3\\lib\\site-packages (4.64.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\elmat\\anaconda3\\lib\\site-packages (from tqdm) (0.4.6)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip available: 22.3.1 -> 23.0\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install tqdm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "from tqdm.notebook import tqdm    # from tqdm import tqdm   # para .py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "84557469903a4216b8c214fa05af43ae",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "  0%|          | 0/377 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wall time: 3min 52s\n"
     ]
    }
   ],
   "source": [
    "%%time\n",
    "\n",
    "for e in tqdm(clean_links):\n",
    "    \n",
    "    index_page(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7: Perform the page indexing in parallel and note the difference in performance.\n",
    "\n",
    "Remember to include `%%time` at the beginning of the cell so that it measures the time it takes for the cell to run."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "import multiprocessing as mp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "ename": "Exception",
     "evalue": "File `'funcion.py'` not found.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\magics\\execution.py\u001b[0m in \u001b[0;36mrun\u001b[1;34m(self, parameter_s, runner, file_finder)\u001b[0m\n\u001b[0;32m    713\u001b[0m             \u001b[0mfpath\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0marg_lst\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 714\u001b[1;33m             \u001b[0mfilename\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfile_finder\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfpath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    715\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\utils\\path.py\u001b[0m in \u001b[0;36mget_py_filename\u001b[1;34m(name, force_win32)\u001b[0m\n\u001b[0;32m    108\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 109\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mIOError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'File `%r` not found.'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    110\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOSError\u001b[0m: File `'funcion.py'` not found.",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<timed eval>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\u001b[0m in \u001b[0;36mrun_line_magic\u001b[1;34m(self, magic_name, line, _stack_depth)\u001b[0m\n\u001b[0;32m   2362\u001b[0m                 \u001b[0mkwargs\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'local_ns'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_local_scope\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstack_depth\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2363\u001b[0m             \u001b[1;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbuiltin_trap\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2364\u001b[1;33m                 \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2365\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2366\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\decorator.py\u001b[0m in \u001b[0;36mfun\u001b[1;34m(*args, **kw)\u001b[0m\n\u001b[0;32m    230\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mkwsyntax\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    231\u001b[0m                 \u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkw\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkw\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msig\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 232\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mcaller\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfunc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mextras\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    233\u001b[0m     \u001b[0mfun\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name__\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    234\u001b[0m     \u001b[0mfun\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\magic.py\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(f, *a, **k)\u001b[0m\n\u001b[0;32m    185\u001b[0m     \u001b[1;31m# but it's overkill for just that one bit of state.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    186\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mmagic_deco\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 187\u001b[1;33m         \u001b[0mcall\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mlambda\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    188\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    189\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mcallable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\magics\\execution.py\u001b[0m in \u001b[0;36mrun\u001b[1;34m(self, parameter_s, runner, file_finder)\u001b[0m\n\u001b[0;32m    723\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'nt'\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mre\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmatch\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mr\"^'.*'$\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mfpath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    724\u001b[0m                 \u001b[0mwarn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'For Windows, use double quotes to wrap a filename: %run \"mypath\\\\myfile.py\"'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 725\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mException\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    726\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    727\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mfpath\u001b[0m \u001b[1;32min\u001b[0m \u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmeta_path\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mException\u001b[0m: File `'funcion.py'` not found."
     ]
    }
   ],
   "source": [
    "%%time\n",
    "\n",
    "%run funcion.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n%%time\\n\\npool=mp.Pool(12)\\n\\nres=pool.map(index_page, tqdm(clean_links))\\npool.close()\\n\\n'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "%%time\n",
    "\n",
    "pool=mp.Pool(12)\n",
    "\n",
    "res=pool.map(index_page, tqdm(clean_links))\n",
    "pool.close()\n",
    "\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": true,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
