\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lecturenotes}[2000/01/29 1.0 (HW)]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions
% single column
%\LoadClass[12pt]{report}
%\RequirePackage[dvips,landscape,a4paper,textwidth=17cm,textheight=17cm,left=1.5cm,top=2.25cm]{geometry}

% page layout for two colums
%\LoadClass[11pt, twocolumn]{report}
%\RequirePackage[a4paper, landscape,textheight=17cm,textwidth=26cm,left=2cm,top=2cm]{geometry}

% page layout for one column, portrait
%\LoadClass[12pt]{report}
%\RequirePackage[a4paper,textheight=26cm,textwidth=17cm,left=2cm,top=2cm]{geometry}

% page layout for slides
\LoadClass[10pt, twoside]{report}
\RequirePackage
[
    papersize={15cm,12cm}, textwidth=13cm, textheight=10.5cm,
    top=0.9cm, headsep=4pt, footskip=10pt
]{geometry}
%\setlength{\headheight}{12pt}
%\setlength{\headsep}{3pt}


\usepackage{lecturenotes}

\RequirePackage{graphicx}
\RequirePackage{natbib}
\RequirePackage{url}
\RequirePackage{color}
\RequirePackage{fancyhdr}
\RequirePackage{listings}
\lstset{language=Python,basicstyle=\small,showstringspaces=false}
\RequirePackage{amsmath,mathtools,amsfonts,amssymb,bm}
%\RequirePackage{amsfonts,amssymb,bm}
%\RequirePackage{indentfirst}
%\RequirePackage{ifthen}
%\RequirePackage[nomarkers, tablesfirst, nolists]{endfloat}%
%\renewcommand{\efloatseparator}{}%{\mbox{}}
%             {\pagestyle{empty}\thispagestyle{empty}\clearpage}

% my customization

\RequirePackage{times}
\renewcommand{\sfdefault}{phv}
\DeclareSymbolFont{letters}{OML}{ptmcm}{m}{it}
\DeclareSymbolFont{operators}{OT1}{ptmcm}{m}{n}

\RequirePackage{setspace}
\RequirePackage{tabulary}
%\newcolumntype{L}{>{\raggedright\arraybackslash}X}%
%\newcolumntype{R}{>{\raggedleft\arraybackslash}X}%
%\renewcommand{\tabularxcolumn}[1]{>{}m{#1}}
%\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
%\newcolumntype{Z}{>{\centering\arraybackslash}X}
\RequirePackage{multirow}
\RequirePackage{multicol}
\RequirePackage[normalem]{ulem}
%\RequirePackage[tight,FIGTOPCAP]{subfigure}
\RequirePackage{subfig}
%\setlength{\subfigcapskip}{-3pt}
%\setlength{\subfigbottomskip}{2pt}
%\setlength{\subfigtopskip}{2pt}
\RequirePackage{rotating}

% endfloat stuff
%\renewcommand{\efloatseparator}{\mbox{}}
%             {\pagestyle{empty}\thispagestyle{empty}\clearpage}
% float customisation
\renewcommand{\textfraction}{0.05}
\renewcommand{\topfraction}{0.95}
\renewcommand{\bottomfraction}{0.95}
\renewcommand{\floatpagefraction}{0.35}
\setcounter{totalnumber}{5}
\setcounter{topnumber}{5}
\setcounter{bottomnumber}{5}
\usepackage{float}
\RequirePackage{wrapfig}
\usepackage{afterpage}
\restylefloat{figure}

% some shorthands
\newcommand{\de}{\ensuremath{^\circ}}
\newcommand{\ie}{\ensuremath{i.e.}}
\newcommand{\eg}{\ensuremath{eg.}}
\newcommand{\dof}{d.o.f.}
\newcommand{\dofs}{d.o.f.s}
\newcommand{\dprod} {\,{\scriptscriptstyle \stackrel{\bullet}{{}}}\,}
\renewcommand{\vec}[1] {\ensuremath{\mathbf #1}}
\newcommand{\gvec}[1] {\ensuremath{\mbox{\boldmath$\bf#1$}}}
\newcommand{\eqn}[1]{\mbox{$#1$}}
\newcommand{\half}{{\ensuremath{^1\negthickspace/\negthinspace_2}}}

% make $\times$, $+$, $-$ and $=$ use less space
\newcommand{\tims}{\negthinspace \times \negthinspace}
\newcommand{\eq}{\negthinspace = \negthinspace}
\newcommand{\plus}{\negthinspace + \negthinspace}
\newcommand{\minus}{\negthinspace - \negthinspace}

% referencing of equation numbers
\newcommand{\eqnRef}[1]{equation (\ref{#1})}
\newcommand{\EqnRef}[1]{Equation (\ref{#1})}

% redefine normalize with different display skips
\renewcommand\normalsize{%
   \@setfontsize\normalsize\@xpt\@xiipt
   \abovedisplayskip 6\p@ \@plus2\p@ \@minus5\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 6\p@ \@plus3\p@ \@minus3\p@
   \belowdisplayskip \abovedisplayskip
   \let\@listi\@listI}


% Space around floats
\setlength{\floatsep}{3pt}
\setlength{\textfloatsep}{3pt}
\setlength{\intextsep}{3pt}
\setlength{\abovecaptionskip}{0pt}
\setlength{\belowcaptionskip}{0pt}

% refer to subsections including the section
\newcommand{\subsec}[2]{\ref{#1}\ref{#2}}
\newcommand{\subsubsec}[3]{\ref{#1}\ref{#2}\ref{#3}}
%\newcommand{\subsec}[2]{\ref{#2}}

% correct way of changing the enumi so that you refer to it properly
%\renewcommand{\theenumi}{\roman{enumi}}
\renewcommand{\labelenumi}{\theenumi.}

%%% modifications to make report style more compact
\makeatletter

%\renewcommand\chaptername{Lecture}
\everymath{\displaystyle}

\def\@makechapterhead#1{
  \clearpage
  \thispagestyle{empty}
  \vspace*{-30pt}%
  {\parindent \z@ \raggedright \normalfont
    \ifnum \c@secnumdepth >\m@ne
        \Large\bfseries \@chapapp\space \thechapter
        :\space
        %\vskip 20\p@
    \fi
    \interlinepenalty\@M
    \Large \bfseries #1\par\nobreak
    %\vskip 6\p@
  }}
\def\@makeschapterhead#1{%
  \vspace*{-30\p@}%
  {\parindent \z@ \raggedright \normalfont
    \Large \bfseries  #1\par\nobreak
    \vskip 6\p@
  }}

\usepackage{fancyhdr}
\pagestyle{fancy}
%\renewcommand{\chaptermark}[1]{\chead[]{\footnotesize\thechapter\space#1}}
\lhead[]{}
\rhead{\footnotesize\thepage}
\cfoot[]{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

%\markright{MTMW12\hfill \chaptermark\hfill}


\def\@part[#1]#2
{
    \refstepcounter{part}
    {
        \parindent \z@ \raggedright \interlinepenalty \@M
        \normalfont \Large\bfseries
        \partname\nobreakspace\thepart : \nobreakspace #2 %\markboth{}{}\par
    }
    \nobreak \vskip 1.3ex \@afterheading
}
\renewcommand\section
{
    \@startsection {section}{1}{\z@}{0.1ex \@plus 0.01ex \@minus -.02ex}%
   {0.01ex \@plus .01ex}{\large\bfseries\raggedright}
}
\renewcommand\subsection
{
    \@startsection {subsection}{2}{\z@}{-0.02ex \@plus -0.01ex \@minus -.02ex}%
   {0.01ex \@plus.01ex}{\normalfont\bfseries\raggedright}
}
\renewcommand\subsubsection
{
    \@startsection {subsubsection}{3}{\z@}{-0.02ex \@plus -0.01ex \@minus -.02ex}%
   {0.01ex \@plus .02ex}{\normalfont\raggedright}
}
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                                    {0.02ex \@plus0.01ex \@minus.02ex}%
                                    {0.01em}%
                                    {\normalfont\normalsize\bfseries}}

\newcommand\bigHeading[1]
{
    \chead{}
    \clearpage
    {\normalfont\Large\bfseries\centering#1\\}
    \normalsize\par
    \nopagebreak\@afterheading
}

\newcommand\heading[1]
{
    {\par\normalfont\Large\bfseries\raggedright#1\par}
    \nopagebreak\@afterheading
}
\newcommand\subheading[1]
{
    {\par\normalfont\large\bfseries\raggedright#1\par}
    \nopagebreak\@afterheading
}
\newcommand\subsubheading[1]
{
    {\par\normalfont\normalsize\bfseries\raggedright#1\par}
    \nopagebreak\@afterheading
}
\newcommand\subsubsubheading[1]
{
    {\par\normalfont\normalsize\bfseries#1}
}

\renewcommand{\maketitle}
{
  \thispagestyle{empty}
  \begin{center}
  \let \footnote \thanks
    {\ \\ \vskip 1em \Large\bf \@title \par}%
    \vskip 2.5em%
    {\large
     % \lineskip 1em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
    %\vskip 0.5em%
    {\large \@date}%

  \end{center}%
  \par
  %\vskip 1.5em
}

\makeatother

\setlength{\marginparwidth}{10 cm}
\setlength{\parindent}{0pt}
\setlength{\parskip}{3pt}

\RequirePackage{tweaklist}
\renewcommand{\itemhook}
{
    \setlength{\topsep}{3pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \setlength{\partopsep}{0pt}
    \setlength{\itemsep}{0pt}
    \setlength{\labelwidth}{10pt}
    \setlength{\leftmargin}{\labelwidth}
}

\renewcommand{\enumhook}
{
    \setlength{\topsep}{3pt}
    \setlength{\parskip}{0pt}
    \setlength{\parsep}{0pt}
    \setlength{\partopsep}{0pt}
    \setlength{\itemsep}{3pt}
    \setlength{\labelwidth}{10pt}
    \setlength{\leftmargin}{\labelwidth}
}


%\renewcommand{\descriptionlabel}[1]{\parbox{\leftmargin}{\raggedleft #1.~}}

% animations
\RequirePackage{hyperref}
\RequirePackage{graphicx}
\RequirePackage{animate}

