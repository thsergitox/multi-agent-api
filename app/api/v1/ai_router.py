from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chatbot_service import ChatbotService
from app.container import Container
import logging

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/chatbot", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chatbot_service: ChatbotService = Depends(lambda: Container.chatbot_service()),
) -> ChatResponse:
    try:
        logger.info(f"Received chat request with message: {request.message[:50]}...")
        response = await chatbot_service.handle_message(request)
        logger.info(f"Successfully processed chat request")
        return response
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/create-latex")
async def create_latex():

    latex = r"""
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{hyperref}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{biblatex} % or \usepackage{natbib} for different bibliography style
\addbibresource{references.bib} % bibliography file

\title{State of the Art in Natural Language Processing}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle
\begin{abstract}
This survey paper provides an overview of the state-of-the-art advancements in Natural Language Processing (NLP). We discuss recent breakthroughs in various subfields including language modeling, machine translation, information retrieval, question answering, and sentiment analysis. This paper also highlights current challenges, benchmarks, and provides insights into promising future research directions.
\end{abstract}

\tableofcontents

\section{Introduction}
Natural Language Processing (NLP) is a rapidly evolving field within artificial intelligence that focuses on enabling computers to understand, interpret, and generate human language. In recent years, the emergence of deep learning, particularly transformer-based models, has led to substantial advancements in NLP applications. This survey aims to review the recent state-of-the-art methods, with an emphasis on transformer architectures, self-supervised learning, and multi-modal NLP. We also address open challenges and discuss potential future directions.

\section{Language Modeling}
Language modeling serves as a foundation for numerous NLP applications. The primary goal is to predict the likelihood of a sequence of words. With the advent of transformer-based models, pre-trained language models have become essential.

\subsection{Transformer Architecture}
The transformer architecture, introduced by Vaswani et al. (2017), is a groundbreaking model that enables efficient parallelization through self-attention mechanisms. Transformers are the backbone of modern NLP models such as BERT, GPT, and T5.

\subsection{Pre-trained Language Models}
Pre-trained language models like BERT, GPT, T5, and RoBERTa have transformed NLP by leveraging vast amounts of text data. These models use unsupervised learning objectives such as masked language modeling (MLM) and autoregressive language modeling (ALM).

\subsubsection{BERT}
BERT (Bidirectional Encoder Representations from Transformers) uses a masked language modeling objective and is bidirectionally trained, which allows it to capture context from both directions.

\subsubsection{GPT and GPT-3}
GPT models are autoregressive, predicting the next word in a sequence. GPT-3, in particular, is notable for its sheer size (175 billion parameters) and its ability to perform few-shot learning.

\subsubsection{T5 and Multitask Models}
The T5 model reframes all NLP tasks as a text-to-text problem, allowing a single architecture to perform multiple tasks. This approach unifies task formats and promotes multi-task learning.

\section{Machine Translation}
Machine translation (MT) is a key NLP task focused on translating text from one language to another. Advances in MT have been driven by sequence-to-sequence models and large-scale transformer architectures.

\subsection{Neural Machine Translation}
Neural machine translation (NMT) uses neural networks to model language sequences. The attention mechanism has significantly improved NMT systems by allowing the model to focus on relevant parts of the input sequence.

\subsection{Transformer-based MT Models}
Transformers have become the standard architecture for NMT. Models like MarianMT, mBART, and multilingual BERT allow translation between multiple languages and have enabled zero-shot translation capabilities.

\section{Information Retrieval and Question Answering}
Information retrieval (IR) and question answering (QA) are two closely related tasks in NLP that focus on retrieving relevant documents or answers in response to a query.

\subsection{Retrieval-based Models}
Traditional IR approaches relied on term-matching and statistical methods, but recent advances use neural embeddings and contextualized representations, as seen in models like DPR (Dense Passage Retrieval).

\subsection{Question Answering Models}
QA models, particularly those based on transformers (e.g., BERT-based QA), have achieved human-level performance on benchmark datasets such as SQuAD. Recent models like T5 and BERT-wwm (whole-word masking) have further improved QA capabilities.

\section{Sentiment Analysis}
Sentiment analysis is the process of identifying and categorizing opinions expressed in text, especially determining the writer's attitude. It has applications in customer feedback analysis, social media monitoring, and market research.

\subsection{Traditional Approaches}
Traditional approaches used lexicons or rule-based systems to infer sentiment, but these methods have limitations in terms of capturing contextual nuances.

\subsection{Neural-based Approaches}
Neural-based sentiment analysis models utilize embeddings and attention mechanisms to capture complex semantic relationships. Pre-trained transformers have proven particularly effective in understanding sentiment contextually.

\section{Benchmarks and Evaluation Metrics}
Evaluating NLP models requires comprehensive benchmarks that capture various language phenomena. Common benchmarks include the GLUE, SuperGLUE, SQuAD, and XNLI datasets.

\subsection{GLUE and SuperGLUE}
GLUE (General Language Understanding Evaluation) and SuperGLUE are popular benchmarks that provide a suite of tasks for evaluating language understanding across diverse tasks.

\subsection{SQuAD}
The Stanford Question Answering Dataset (SQuAD) is widely used for benchmarking QA models. It provides passages and questions, with models evaluated based on answer extraction accuracy.

\section{Challenges and Open Problems}
Despite the remarkable progress, NLP faces several challenges, including bias in language models, handling low-resource languages, and improving model interpretability.

\subsection{Bias in Language Models}
Large-scale language models often exhibit social biases present in the training data, which can lead to unintended consequences in applications.

\subsection{Low-resource Languages}
Many NLP advancements are focused on high-resource languages, leaving low-resource languages underserved. Multilingual and transfer learning approaches are being explored to address this gap.

\subsection{Interpretability}
The interpretability of complex models like transformers remains a challenge, as these models operate as "black boxes." Techniques like attention visualization and saliency maps are promising but limited.

\section{Future Directions}
Future work in NLP may focus on advancing multi-modal learning, improving model efficiency, and fostering responsible AI practices.

\subsection{Multi-modal NLP}
Integrating text with other modalities, such as images and speech, offers exciting potential for richer representations and better context understanding.

\subsection{Efficient NLP Models}
With the increasing size of models, there is a need for efficient NLP methods that reduce computational cost without compromising accuracy.

\section{Conclusion}
This survey highlights the current state-of-the-art in NLP, covering advancements in language modeling, machine translation, question answering, and other areas. While substantial progress has been made, there remain significant challenges and opportunities for future research.

\printbibliography

\end{document}
"""

    return {"latest": latex}