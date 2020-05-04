\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{itesoinvrep05}[2017/05/29 ITESO investigation report]

\LoadClass[letterpaper,12pt,twoside]{book}

\usepackage{geometry}
%\geometry{letterpaper, margin=1in}
\geometry{letterpaper, tmargin=1in,bmargin=1in,lmargin=1in,rmargin=1in}
%\usepackage{showframe}  %Muestra los margenes visualmente

\RequirePackage{etoolbox}

%\BeforeBeginEnvironment{equation}{\par\setstretch{0.6}\selectfont}
%\AfterEndEnvironment{equation}{\setstretch{1.5}\selectfont}

%Espacio de Ecuaciones. 
\usepackage{amsmath}
\expandafter\def\expandafter\normalsize\expandafter{%
    \normalsize
    \setlength\abovedisplayskip{5pt}
    \setlength\belowdisplayskip{5pt}
    \setlength\abovedisplayshortskip{5pt}
    \setlength\belowdisplayshortskip{7pt}
}

\RequirePackage{ifthen}

% color
\RequirePackage{xcolor}

% graphics
\RequirePackage{graphicx}

\RequirePackage{changepage}

\renewcommand{\baselinestretch}{1.5}
\setlength\parindent{1.25cm}
\setlength\parskip{0em}

%algorithms
\usepackage{algorithm}
\usepackage{algpseudocode}

%captions packet
\RequirePackage{caption}

%Bibliography
\RequirePackage{cite}
\bibliographystyle{IEEEtran}


\let\oldthebibliography\thebibliography
\renewenvironment{thebibliography}[1]{
  \begin{oldthebibliography}{#1}
    \setlength{\itemsep}{6pt}
    \setlength{\parskip}{0pt}
    \setstretch{1}\fontsize{11.2}{12.0}\selectfont
  }
 {
  \end{oldthebibliography}
 }

\def\bibindent{1em}
\let\old@biblabel\@biblabel
\def\@biblabel#1{\old@biblabel{#1}\kern\bibindent}

%definitions
\def\abstractname{Abstract}

% headers and footers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\newlength\FHoffset
\setlength\FHoffset{0cm}
%\addtolength\headwidth{2\FHoffset}

\fancyheadoffset{\FHoffset}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\fancyfoot{}
\fancyfoot[RE]{\fontsize{10}{1}\selectfont ITESO}
\fancyfoot[CE]{\fontsize{10}{1}\selectfont\thepage}

\fancypagestyle{cover}{%
	\fancyhf{} % clear all header and footer fields
	\lfoot{}
	\cfoot{}
	\rfoot{}
}

\fancypagestyle{firstpage}{%
	\fancyhf{} % clear all header and footer fields
    \fancyfoot[L]{\fontsize{10}{1}\selectfont ITESO}
    \fancyfoot[C]{\fontsize{10}{1}\selectfont\thepage}
	\renewcommand{\headrulewidth}{0pt}
}

\usepackage[T1]{fontenc}
%\usepackage[letterpaper, tmargin=1in,bmargin=1in,lmargin=1in,rmargin=1in]{geometry}
\usepackage{setspace}
\usepackage{ragged2e}
\usepackage{indentfirst}

\usepackage{mathptmx} %Agregamos para la letra Time New Roma

%Appendix of Files
\usepackage{newfloat}
\DeclareFloatingEnvironment[placement={!hb},name=AppendixFile]{appendixfile}


%Mover Imagenes al final
\providetoggle{holdfloat}
\settoggle{holdfloat}{false}
	
\DeclareOption{holdfloat}{
	\settoggle{holdfloat}{true}
}
\ProcessOptions\relax

\iftoggle{holdfloat}{}{
	\usepackage[nolists,nomarkers,tablesfirst]{endfloat}
	\renewcommand{\efloatseparator}{\mbox{}}
	\DeclareDelayedFloat{algorithm}{Algorithm}
	\DeclareDelayedFloat{appendixfile}{AppendixFiles}
	\SetupDelayedFloat{appendixfile}{nolist,nohead}
}


%BlankPage 
\def\blankpage{%
      \clearpage%
      \thispagestyle{empty}%
      \addtocounter{page}{-1}%
      \null%
      \clearpage}


%href for email
\usepackage[colorlinks=true,linkcolor=black,urlcolor=blue,citecolor=black]{hyperref}

%reduce space between letters and lines
\usepackage{microtype}

% Fields definition
%\renewcommand*{\author}[1]{\def\@author{#1}}
%\newcommand*{\cvu}[1]{\def\@cvu{#1}}
\newcommand*{\director}[1]{\def\@director{#1}}
\renewcommand*{\title}[1]{\def\@titulo{#1}}
%\renewcommand*{\title}[1]{\def\@title{#1}}
\newcommand*{\itesoshield}[1]{\def\@itesoshield{#1}}
\newcommand*{\FechaDocumento}[1]{\def\@FechaDocumento{#1}}
%\newcommand*{\DocumentDate}[1]{\def\@DocumentDate{#1}}

% Cover Page - Spanish
\newcommand{\makeitesocoverpage}[0]{
	\thispagestyle{cover}
	%\addtocounter{page}{-1}
	\setstretch{1.0}
	\begin{center}

	{\fontsize{20}{20}\selectfont \textls[-65]{\textbf{INSTITUTO TECNOLÓGICO Y DE ESTUDIOS SUPERIORES DE OCCIDENTE}}\par}

	{\fontsize{14}{18}\selectfont \textls[-65]{Reconocimiento de valiz oficial de estudios de nivel superior según acuerdo secretarial 15018, publicado en el Diario Oficial de la Federación el 29 de noviembre de 1976.}\par}
	\hrule
	
	\\[24pt]
	
	{\fontsize{14}{18}\selectfont \textls[-65]{Departamento de Electrónica, Sistemas e Informática}}
	\\[14pt]	
	
	{\fontsize{14}{18}\selectfont \textls[-65]{\textsc{Maestría en Sistemas Computacionales}}}
	\\[15pt]

	%\begin{figure*}[h!]
	\centering
  	\includegraphics[width=1.67in, height=1.67in]{\@itesoshield}
	%\end{figure}

	\\[24pt]
	
	{\fontsize{14}{18}\selectfont \textls*[10]{\MakeUppercase{\@titulo}}\par}
	\\[24pt]

	{\fontsize{14}{18}\selectfont \textls[-65]{Trabajo recepcional que para obtener el grado de}\par}
	{\fontsize{14}{18}\selectfont \textls[-65]{Maestra en Sistemas Computacionales}}
	\\[15pt]
	\\
	{\fontsize{14}{18}\selectfont Presenta: \@author \par}
	%{\fontsize{14}{18}\selectfont CVU: \@cvu}
	\\[12pt]
	\\
	{\fontsize{14}{18}\selectfont Asesor: \@director}
	\\[12pt]

    \vfill

	\end{center}

    \begin{flushright}
	{\fontsize{14}{18}\selectfont Tlaquepaque, Jalisco a \@FechaDocumento}
	\end{flushright}
	\newpage
}

\renewcommand{\maketitle}[0]{
	\makeitesocoverpage
	\makeitesocoverpageenglish
	%\blankpage
	%\makeitesotitle
	%\vspace{-3.0em}
	\setstretch{1.5}
	\justify
}

% MAINMATTER
\newcommand{\mainmatterSU}{

\begingroup
\cleardoublepage
\edef\x{\endgroup
\noexpand\mainmatter
\setcounter{page}{\the\value{page}}%
}%
\x

%\cleardoublepage

\fancypagestyle{plain}
{
    \fancyhead{}
    \fancyfoot[LE,RO]{{\fontfamily{verdana}\selectfont\thepage}}
}	% re-define plain page

\pagestyle{fancy}
\fancyhf{}
\fancyfoot[LE,RO]{{\fontfamily{verdana}\selectfont\thepage}}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
}