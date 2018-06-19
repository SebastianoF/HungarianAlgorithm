%----------------------------------------------------
%
%  ClasseMatematicamente.cls 
%  update 23_3_2014 versione beta
%
%_____________________________________________________

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ClasseMatematicamente}[2014/03/23 v0.0 LaTeX class for matematicamente.it]

\DeclareOption*{%
\PassOptionsToClass{\CurrentOption}{article}%
}

\ProcessOptions\relax

\LoadClass[twoside]{article}

\RequirePackage[usenames,dvipsnames]{color}
\RequirePackage{fancyhdr}
\RequirePackage{graphicx}


%-------- pacchetti base------------------
\usepackage[english]{babel}
\usepackage{euscript}
\usepackage[utf8]{inputenc}
%------ per i diagrammi commutativi: 
\usepackage{pictexwd,dcpic}
\usepackage[all]{xy}
% per altri fon

%\usepackage[sc]{mathpazo}

%________________________________________

%------------------- settings margini ----
\setlength{\oddsidemargin}{-20pt}
\setlength{\evensidemargin}{-20pt}
\setlength{\marginparwidth}{0pt}
\setlength{\textwidth}{510pt}
\setlength{\topmargin}{-20pt}
\setlength{\textheight}{610pt}
%-- decommentare per risettare i margini:
%\usepackage{showframe}
%_____________________________________

%--------------- ausiliari cambiare font

\newcommand{\cambiaFont}[2]{{\fontencoding{T1}\fontfamily{#1}%
\selectfont#2}}
%per un elenco dei fotns copiare la parte commentata in fondo a questo .cls nel documento .tex e compilare. 

%er cambiare il colore dei titoli>
\usepackage{xcolor}
\usepackage{sectsty}
\chapterfont{\color{MidnightBlue}}  % sets colour of chapters
\sectionfont{\color{MidnightBlue}}
\subsectionfont{\color{MidnightBlue}}
\subsubsectionfont{\color{MidnightBlue}}

%--------------- ausiliari fancyheaders  ----

\newcommand{\HeadingNumeroInfo}{}
\newcommand{\HeadingNumero}[1]{\renewcommand{\HeadingNumeroInfo}{#1}}

\newcommand{\HeadingDataInfo}{}
\newcommand{\HeadingData}[1]{\renewcommand{\HeadingDataInfo}{#1}}
 
\newcommand{\HeadingSito}{
 \color{MidnightBlue} \cambiaFont{ppl}{  Matematicamente.it ~ Magazine } \color{MidnightBlue}
}

% ------------ ausiliari titolo -----------

\newcommand{\NumeroArticoloInfo}{}
\newcommand{\NumeroArticolo}[1]{\renewcommand{\NumeroArticoloInfo}{#1}}

\newcommand{\TitoloInfo}{}
\newcommand{\Titolo}[1]{\renewcommand{\TitoloInfo}{#1}}

  \newcommand{\AutoreAInfo}{}
  \newcommand{\AutoreA}[1]{\renewcommand{\AutoreAInfo}{#1}}
  \newcommand{\EmailAInfo}{}
  \newcommand{\EmailA}[1]{\renewcommand{\EmailAInfo}{#1}}
%
 \newcommand{\AutoreBInfo}{}
 \newcommand{\AutoreB}[1]{\renewcommand{\AutoreBInfo}{#1 }}
 \newcommand{\EmailBInfo}{}
 \newcommand{\EmailB}[1]{\renewcommand{\EmailBInfo}{#1}}
% 
 \newcommand{\AutoreCInfo}{}
 \newcommand{\AutoreC}[1]{\renewcommand{\AutoreCInfo}{#1}}
 \newcommand{\EmailCInfo}{}
 \newcommand{\EmailC}[1]{\renewcommand{\EmailCInfo}{#1}}
% 
 \newcommand{\AutoreDInfo}{}
 \newcommand{\AutoreD}[1]{\renewcommand{\AutoreDInfo}{#1}}
 \newcommand{\EmailDInfo}{}
 \newcommand{\EmailD}[1]{\renewcommand{\EmailDInfo}{#1}}
% 
 \newcommand{\AutoreEInfo}{}
 \newcommand{\AutoreE}[1]{\renewcommand{\AutoreEInfo}{#1 }}
 \newcommand{\EmailEInfo}{}
 \newcommand{\EmailE}[1]{\renewcommand{\EmailEInfo}{#1 }} 

\newcommand{\DedicaInfo}{}
\newcommand{\Dedica}[1]{\renewcommand{\DedicaInfo}{#1}}


%____________________________________________

%-------------------- titolo -----------------

\newcommand{\Issue}{
  ~  %\vspace{0.5cm}  
  \begin{flushleft}
  {\Huge  \NumeroArticoloInfo .~\TitoloInfo } 
  \end{flushleft}

  \begin{flushright}
  {\Large 
  % un ciclo for risolverebbe il problema... Mettere nelle prossime versioni della classe!
   \AutoreAInfo \\   
   \EmailAInfo  %\\ 
   %\AutoreBInfo \\
   %\EmailBInfo %\\
   %\AutoreCInfo \\
   %\EmailCInfo \\
   %\AutoreDInfo \\
   %\EmailDInfo \\
   %\AutoreEInfo \\
   %\EmailDInfo 
  }
  \end{flushright}
  
  \vspace{0.2in}
  
  \begin{flushleft}
  {\small
  \emph{\DedicaInfo}
  }
  \end{flushleft} 
  
  \vspace{0.4in}
}

%______________________________________________


%------------ fancyheaders -----------------
\fancyhead{} % clear all header fields
\fancyhead[C]{ \HeadingSito \\ \cambiaFont{ppl}{ \color{MidnightBlue} $\bullet$ \color{OrangeRed} ~\HeadingNumeroInfo ~- \HeadingDataInfo ~ \color{MidnightBlue}$\bullet$\color{black}} \vspace{0.2cm}}
\renewcommand{\headrulewidth}{0.1pt}
%----------- fancyfooters ---------------
\fancyfoot{} % clear all footer fields
\fancyfoot[C]{\color{MidnightBlue}  {\bf \thepage} \color{black} }
%___________________________________________________





%------------ Teoremi, impaginazioni matematiche --------

\newtheorem{definition}{Definition}
\newtheorem{esempio}{Esempio}%[section]
\newtheorem{lemma}{Lemma}%[section]
\newtheorem{osservazione}{Osservazione}%[section]
\newtheorem{quest}{Questione}%[section]
\newtheorem{theor}{Theorem}%[section]
\newtheorem{prop}{Property}%[section]
\newtheorem{corollario}[theor]{Corollario}
\newtheorem{algo}{Algritmo}

%---------- Dimostrazione in italiano
\newenvironment{proof}{\par\addvspace\topsep\noindent
{\bf Proof:} \ignorespaces }{\qed}
\newcommand{\qed}{\hspace*{\fill}$\Box$\ifmmode\else\par\addvspace\topsep\fi}

%----------  Ridefinizione per il quoziente:
\def\quotient#1#2{%
    \raise1ex\hbox{$#1$}\Big/\lower1ex\hbox{$#2$}%
}

%______________________________________________________


\usepackage{listings}
\usepackage{color}

\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}

\lstset{ %frame=tb,
	language=Python,
	aboveskip=3mm,
	belowskip=3mm,
	showstringspaces=false,
	columns=flexible,
	basicstyle={\small\ttfamily},
	numbers=none,
	numberstyle=\tiny\color{gray},
	keywordstyle=\color{blue},
	commentstyle=\color{dkgreen},
	stringstyle=\color{mauve},
	breaklines=false,
	breakatwhitespace=true,
	tabsize=3
}




%_______________________________FINE_____________________________

% Utilità: i possibili fonts a disposizione con il comando \cambiaFont 

% \begin{itemize}
%  \item quelli con grazie (spesso usati nel corpo principale dei
%  documenti)
%   \begin{itemize}
%    \item \cambiaFont{fve}{il Bera Serif;}
%    \item \cambiaFont{pbk}{il Bookman;}
%    \item \cambiaFont{bch}{il Charter;}
%    \item \cambiaFont{pnc}{il New Century Schoolbook;}
%    \item \cambiaFont{ptm}{il Times (molto comune);}
%    \item \cambiaFont{ppl}{il Palatino (bellissimo!);}
%    \item \cambiaFont{put}{l'Utopia;}
%    \item \cambiaFont{pzc}{lo Zapf Chancery.}
%   \end{itemize}
%  \item quelli senza grazie (spesso usati nei titoli, nelle
%  didascalie, nelle testatine, ecc.)
%   \begin{itemize}
%    \item \cambiaFont{ua1}{l'Arial (molto comune);}
%    \item \cambiaFont{pag}{l'Avant Garde (bellissimo per i titoli; lo
%    si vede molto spesso in giro);}
%    \item \cambiaFont{fvs}{il Bera Sans Serif;}
%    \item \cambiaFont{phv}{l'Helvetica (anche questo molto comune);}
%    \item \cambiaFont{iwona}{l'Iwona (molto bello soprattutto in
%    \MakeUppercase{maiuscolo} o in \textsc{maiuscoletto}).}
%   \end{itemize}
%  \item quelli a mo' di macchina da scrivere (spesso usati per
%  rappresentare i listati dei programmi)
%   \begin{itemize}
%    \item \cambiaFont{fvm}{il Bera Mono;}
%    \item \cambiaFont{pcr}{il Courier (decisamente un po' troppo in
%    grande).}
%   \end{itemize}
% \end{itemize}
