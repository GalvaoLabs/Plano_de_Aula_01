"""
Plano de Aula — Entre Emoções e Escolhas
Site em Streamlit para a palestra participativa sobre amor e relacionamentos.

Para rodar:
    pip install streamlit
    streamlit run app.py
"""

import streamlit as st

# ──────────────────────────────────────────────────────────────────────────
# PALETA DE CORES
# ──────────────────────────────────────────────────────────────────────────
PALETTE = {
    "bg": "#0f0f13",
    "card": "#18181f",
    "accent": "#e8445a",
    "accent2": "#f4a261",
    "text": "#f0eee9",
    "muted": "#9b9aa3",
    "border": "#2a2a35",
    "green": "#52c77e",
    "blue": "#5b9cf6",
    "purple": "#a78bfa",
    "teal": "#4fd1c5",
}

ANCHOR_COLORS = {
    "Todos": PALETTE["green"],
    "Professora + Todos": PALETTE["teal"],
    "Miguel + Maria Clara": PALETTE["accent2"],
    "Professora": PALETTE["teal"],
    "Miguel": PALETTE["blue"],
    "Maria Clara": PALETTE["accent"],
}


def anchor_color(anchor: str) -> str:
    return ANCHOR_COLORS.get(anchor, PALETTE["muted"])


# ──────────────────────────────────────────────────────────────────────────
# DADOS — ESTRUTURA DA AULA
# ──────────────────────────────────────────────────────────────────────────
AULA1 = [
    {
        "num": "01",
        "title": "Abertura e Apresentação",
        "time": "7 min",
        "anchor": "Professora",
        "content": [
            "Sala já organizada em formato U antes de começar (combinar com a professora antes)",
            "Professora dá boas-vindas à turma e apresenta Miguel e Maria Clara",
            "Miguel e Maria Clara se apresentam brevemente — quem são e por que estão ali",
            "Combinar as regras: respeito, ninguém é obrigado a responder, celulares guardados",
            'Frase de abertura (Miguel): "Hoje não é uma aula — é uma conversa. Sobre amor, escolhas e o que fazemos com o que sentimos."',
        ],
    },
    {
        "num": "02",
        "title": "Três Visões sobre o Amor: Kafka, Dostoiévski e C.S. Lewis",
        "time": "12 min",
        "anchor": "Miguel + Maria Clara",
        "content": [
            'Projetar no slide — Kafka: "Eu fugi do amor porque sabia que ele me destruiria."',
            'Projetar no slide — Dostoiévski: "Eu corri em direção ao amor porque precisava dele para destruir quem eu costumava ser."',
            'Projetar no slide — C.S. Lewis (Os Quatro Amores, tradução livre): "Amar de qualquer forma é se tornar vulnerável."',
            "Miguel pergunta à turma: qual das três frases mais se parece com o que vocês sentem hoje? Por quê?",
            "Deixar 3–4 minutos de debate espontâneo — não dar resposta certa",
            "Maria Clara anota as palavras que a turma fala na lousa",
            'Maria Clara conecta: "Fugir, entregar-se ou aceitar o risco — três formas diferentes de lidar com o mesmo medo de se machucar."',
        ],
    },
    {
        "num": "03",
        "title": "O que é Amor para você?",
        "time": "8 min",
        "anchor": "Maria Clara",
        "content": [
            "Perguntas rápidas e espontâneas para a sala",
            "Maria Clara conduz a rodada de respostas e complementa as palavras na lousa",
            'Conectar com as citações: "Olha o que vocês disseram — agora comparem com Kafka, Dostoiévski e Lewis."',
            "Objetivo: mostrar que o conceito de amor é subjetivo e construído",
        ],
    },
    {
        "num": "04",
        "title": "Paixão, Amor e os Quatro Amores de C.S. Lewis",
        "time": "14 min",
        "anchor": "Miguel",
        "content": [
            "Paixão: intensa, rápida, impulsiva, idealiza a pessoa",
            "Amor: construção, paciência, responsabilidade, constância",
            "Apresentar rapidamente os quatro tipos de amor descritos por C.S. Lewis: Storge (afeto familiar), Philia (amizade), Eros (paixão romântica) e Ágape (amor incondicional, que dá sem cobrar volta)",
            'C.S. Lewis sobre a amizade (tradução livre): "A amizade não é necessária para viver — mas é uma das coisas que dão valor à vida."',
            '"Uma pessoa pode gostar muito de alguém e ainda assim fazer mal?"',
            '"Ciúme é prova de amor?" / "Dá para amar sem maturidade?"',
            'Maria Clara provoca: "Será que qualquer um desses quatro amores pode virar tóxico se for levado ao extremo?"',
        ],
    },
    {
        "num": "05",
        "title": "Amor e Redes Sociais",
        "time": "8 min",
        "anchor": "Maria Clara",
        "content": [
            "Relacionamentos 'de aparência' e pressão para namorar cedo",
            "Comparação com casais idealizados na internet",
            "Dependência emocional e exposição exagerada",
            '"As redes sociais mostram relacionamentos reais?" / "Existe pressão para namorar cedo?"',
        ],
    },
    {
        "num": "06",
        "title": "Fechamento da 1ª Aula",
        "time": "6 min",
        "anchor": "Professora + Todos",
        "content": [
            'Professora retoma as citações: "Kafka fugiu. Dostoiévski correu. Lewis avisou que os dois estavam arriscando o coração — e que não tem como amar sem isso."',
            'Miguel fecha: "Sentir é natural. Aprender a lidar com o que sentimos — isso é maturidade."',
            "Avisar que a segunda parte vai ser mais profunda e pessoal",
        ],
    },
]

AULA2 = [
    {
        "num": "07",
        "title": "Amor-próprio e Identidade",
        "time": "13 min",
        "anchor": "Maria Clara",
        "content": [
            "Entrar em relacionamentos por carência vs. por escolha",
            "Necessidade de aprovação e medo de ficar sozinho",
            "Autoestima: como me vejo afeta como me relaciono",
            '"É possível amar alguém sem se valorizar?" / "Por que algumas pessoas aceitam relações ruins?"',
            'Retomar Dostoiévski: "Ele disse que o amor o destruiu para reconstruí-lo — amadurecimento ou dependência?"',
        ],
    },
    {
        "num": "08",
        "title": "Relacionamentos Saudáveis x Tóxicos",
        "time": "12 min",
        "anchor": "Miguel",
        "content": [
            "Saudável: diálogo, respeito, liberdade, confiança, apoio mútuo",
            "Tóxico: controle, humilhação, manipulação, ciúme excessivo",
            '"Mexer no celular do outro é normal?" / "Ciúme é cuidado ou controle?"',
            "Retomar os Quatro Amores: até o Storge (afeto) e o Eros (paixão) podem virar posse se perderem o respeito",
            'Maria Clara complementa: "Até onde vai o limite do amor?"',
        ],
    },
    {
        "num": "09",
        "title": "Dinâmica: Os Quatro Amores na Prática",
        "time": "10 min",
        "anchor": "Todos",
        "content": [
            "Dividir a turma em quatro grupos: Storge, Philia, Eros e Ágape",
            "Cada grupo lista exemplos reais da própria vida que se encaixam naquele tipo de amor (família, amigos, namoro, um gesto de generosidade sem retorno)",
            "Miguel e Maria Clara circulam entre os grupos ajudando e provocando com perguntas",
            "Um representante de cada grupo compartilha um exemplo com a turma toda",
            "Objetivo: mostrar que 'amor' não é uma coisa só, e que o romance é apenas uma fatia pequena do que sentimos no dia a dia",
        ],
    },
    {
        "num": "10",
        "title": "Dinâmica: Concordo ou Discordo",
        "time": "10 min",
        "anchor": "Todos",
        "content": [
            "Miguel e Maria Clara falam frases em revezamento — alunos levantam a mão",
            'Miguel: "Ciúme é prova de amor."',
            'Maria Clara: "Quem ama perdoa tudo."',
            'Miguel: "É melhor namorar cedo para ganhar experiência."',
            'Maria Clara: "Uma amizade pode ser mais forte que um namoro."',
            'Miguel: "Kafka tinha razão em fugir do amor."',
            "Comentar as respostas sem julgar — o objetivo é gerar reflexão coletiva",
        ],
    },
    {
        "num": "11",
        "title": "Encerramento Final",
        "time": "10 min",
        "anchor": "Todos",
        "content": [
            'Miguel: "Amor não é só emoção — sentimentos precisam de responsabilidade."',
            'Maria Clara: "Maturidade emocional importa. Respeito vem antes do romance."',
            'Professora fecha com a turma: "Em uma palavra — o que vocês levam dessa conversa?"',
            "Agradecer a participação da sala",
        ],
    },
]

DIVISAO = [
    {
        "name": "Miguel",
        "color": PALETTE["blue"],
        "blocks": [
            "Abertura conjunta — se apresenta à turma (bloco 01)",
            "Conduz o debate das três citações (bloco 02)",
            "Paixão, Amor e os Quatro Amores — bloco principal (bloco 04)",
            "Relacionamentos Saudáveis x Tóxicos — bloco principal (bloco 08)",
            "Fala na dinâmica Concordo/Discordo (bloco 10)",
            "Primeira fala do encerramento (bloco 11)",
        ],
    },
    {
        "name": "Maria Clara",
        "color": PALETTE["accent"],
        "blocks": [
            "Abertura conjunta — se apresenta à turma (bloco 01)",
            "Anota as palavras da turma na lousa e conecta as citações (bloco 02)",
            "Conduz 'O que é Amor?' — pergunta à turma (bloco 03)",
            "Provoca sobre os limites dos Quatro Amores (bloco 04)",
            "Amor e Redes Sociais — bloco principal (bloco 05)",
            "Amor-próprio e Identidade — bloco principal (bloco 07)",
            "Complemento em Relacionamentos Saudáveis x Tóxicos (bloco 08)",
            "Fala na dinâmica Concordo/Discordo (bloco 10)",
            "Segunda fala do encerramento (bloco 11)",
        ],
    },
    {
        "name": "Professora",
        "color": PALETTE["teal"],
        "blocks": [
            "Organiza a sala em formato U antes da palestra começar",
            "Recebe a turma e apresenta Miguel e Maria Clara (bloco 01)",
            "Retoma as três citações no fechamento da 1ª aula (bloco 06)",
            "Fecha a palestra puxando uma palavra de cada aluno (bloco 11)",
            "Apoio geral: ajuda a mediar o tempo entre os blocos e acalma a turma se necessário",
        ],
    },
]

CITACOES = [
    {
        "author": "Franz Kafka",
        "color": PALETTE["blue"],
        "quote": "Eu fugi do amor porque sabia que ele me destruiria.",
        "analise": [
            "Kafka via o amor como ameaça à sua identidade e estabilidade",
            "Representa quem tem medo de se perder em uma relação",
            "Pergunta: fugir do amor é covardia ou autoconhecimento?",
            "Conectar com: medo de se machucar, proteção emocional, fechamento afetivo",
        ],
    },
    {
        "author": "Fiódor Dostoiévski",
        "color": PALETTE["accent"],
        "quote": "Eu corri em direção ao amor porque precisava dele para destruir quem eu costumava ser.",
        "analise": [
            "Dostoiévski via o amor como agente de transformação — necessário, mesmo doloroso",
            "Representa quem usa as relações para crescer e se reinventar",
            "Pergunta: amar para mudar é saudável ou é dependência?",
            "Conectar com: busca de identidade, amadurecimento, relações como espelho",
        ],
    },
    {
        "author": "C.S. Lewis — Os Quatro Amores",
        "color": PALETTE["purple"],
        "quote": "Amar de qualquer forma é se tornar vulnerável. (tradução livre)",
        "analise": [
            "Lewis não escolhe entre fugir (Kafka) ou se entregar (Dostoiévski) — ele nomeia o risco que os dois estão, de formas opostas, tentando administrar",
            "Para ele, a única forma de blindar o coração de qualquer dor é não amar nada — e isso, para Lewis, é o maior risco de todos",
            "Pergunta: dá para amar sem se expor? Vale a pena tentar?",
            "Conectar com: coragem emocional, blindagem afetiva, o preço de se importar com alguém",
        ],
    },
]

QUATRO_AMORES = [
    ("Storge", "afeto — o amor de família, o carinho que nasce do convívio e do tempo junto"),
    ("Philia", "amizade — o amor entre pessoas que escolhem caminhar lado a lado"),
    ("Eros", "paixão romântica — o amor que deseja e se apaixona por alguém específico"),
    ("Ágape", "amor incondicional — o que dá sem esperar nada em troca"),
]

FAQ = [
    {
        "question": "Amizade também é uma forma de amor?",
        "answer": [
            "Sim — para C.S. Lewis, a amizade (Philia) é um dos quatro tipos de amor, tão real quanto o romântico",
            "Diferente do Eros, a amizade não depende de exclusividade nem de atração — mas exige escolha e presença igualmente",
            "Vale perguntar à turma: 'quantos de vocês diriam que amam um amigo?' — normalmente poucos usam essa palavra, e essa é a provocação",
        ],
        "link": "bloco 04 (Os Quatro Amores)",
    },
    {
        "question": "Dá para amar sem sofrer?",
        "answer": [
            "Segundo Lewis, não — amar de qualquer forma é se expor a ser magoado, porque amar é dar controle do próprio bem-estar a outra pessoa",
            "A alternativa que ele descreve — blindar o coração para nunca sofrer — também tem um preço: isolamento",
            "A conversa não é 'como evitar sofrer', e sim 'como lidar bem quando doer'",
        ],
        "link": "bloco 02 (citação de Lewis)",
    },
    {
        "question": "Por que um amor 'bom' às vezes também machuca?",
        "answer": [
            "Existe diferença entre a dor do crescimento (um desentendimento, uma cobrança justa, um limite colocado) e a dor do abuso (controle, humilhação, medo)",
            "Pergunta para deixar no ar: 'essa dor está me fazendo crescer ou está me diminuindo?'",
            "Reforçar que discordar não é sinônimo de toxicidade — o problema é o desrespeito, não o desconforto",
        ],
        "link": "bloco 08 (Saudável x Tóxico)",
    },
    {
        "question": "Existe 'a pessoa certa' logo de cara?",
        "answer": [
            "A ideia de 'amor à primeira vista' geralmente descreve paixão, não amor — e paixão é apenas o início possível de uma história, não uma garantia",
            "Amor, no sentido de compromisso e construção, se prova com tempo, não com intensidade inicial",
            "Reforçar: não tem problema nenhum não saber ainda — maturidade emocional também é sobre paciência consigo mesmo",
        ],
        "link": "bloco 04 (Paixão x Amor)",
    },
    {
        "question": "Ciúme é sempre errado?",
        "answer": [
            "Sentir ciúme não é o problema — é uma reação emocional comum. O problema é o que se faz com ele",
            "Ciúme que gera diálogo ('isso me incomodou, posso te contar por quê?') é diferente de ciúme que vira controle (mexer no celular, restringir amizades)",
            "Vale conectar com o Storge e o Eros: até o afeto mais genuíno pode escorregar para posse se perder o respeito pelo outro",
        ],
        "link": "bloco 08 (Saudável x Tóxico)",
    },
    {
        "question": "Por que as redes sociais fazem o amor parecer perfeito?",
        "answer": [
            "O que aparece online é geralmente o ponto alto editado, não o relacionamento inteiro — brigas, rotina e desentendimentos não viram post",
            "Comparar a própria vida com a versão editada da vida do outro é uma comparação injusta por definição",
            "Perguntar: 'vocês postariam uma discussão com o namorado(a)? então por que comparam a sua realidade com o destaque de outra pessoa?'",
        ],
        "link": "bloco 05 (Amor e Redes Sociais)",
    },
]

DICAS = [
    ("📜", "Projetar as três citações (Kafka, Dostoiévski, Lewis) em slide — impacta mais do que só falar"),
    ("📖", "Usar os Quatro Amores de C.S. Lewis como fio condutor da aula: cada bloco pode ser relembrado como Storge, Philia, Eros ou Ágape"),
    ("🖥", "Slides com pouco texto — frases curtas, imagens e perguntas"),
    ("🔄", "Interação a cada 5–8 min — adolescentes perdem atenção rápido"),
    ("🎵", "Música instrumental leve enquanto organizam a sala em U"),
    ("💡", "Frase marcante: 'Nem todo sentimento saudável é intenso. E nem toda intensidade é saudável.'"),
    ("📐", "Combinar com a professora para a sala já estar em U antes da palestra começar"),
    ("🙋", "Guardar 2–3 minutos ao final para puxar uma pergunta da aba 'Perguntas Frequentes' caso a turma fique quieta"),
]

AVOID = [
    "Transformar em sermão moralista",
    "Debate religioso direto (mesmo citando Lewis — o foco é a reflexão, não a fé)",
    "Expor experiências pessoais delicadas",
    "Pressionar alunos tímidos a responder",
    "Fazer piadas excessivas sobre namoro",
    "Falar como 'coach' ou dar conselhos prontos",
    "Deixar o debate das citações se estender além do tempo",
    "Encerrar a dinâmica dos Quatro Amores sem deixar cada grupo compartilhar pelo menos um exemplo",
]

LEGENDA_ANCORAS = [
    (PALETTE["blue"], "Miguel"),
    (PALETTE["accent"], "Maria Clara"),
    (PALETTE["teal"], "Professora"),
    (PALETTE["green"], "Todos"),
]


# ──────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA E CSS
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Entre Emoções e Escolhas — Plano de Aula",
    page_icon="💬",
    layout="centered",
)

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {PALETTE["bg"]};
            color: {PALETTE["text"]};
        }}
        html, body, [class*="css"] {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }}
        .block-container {{
            max-width: 720px;
            padding-top: 1.5rem;
        }}
        /* Header */
        .plano-header {{
            background: linear-gradient(135deg, #1a0a10 0%, {PALETTE["bg"]} 60%);
            border: 1px solid {PALETTE["border"]};
            border-radius: 18px;
            padding: 30px 26px 24px;
            margin-bottom: 24px;
        }}
        .plano-eyebrow {{
            font-size: 11px; color: {PALETTE["accent"]}; letter-spacing: 2px;
            text-transform: uppercase; margin-bottom: 8px;
        }}
        .plano-title {{
            font-family: Georgia, serif; font-size: 32px; font-weight: 700;
            color: #fff; line-height: 1.2; margin: 0 0 8px;
        }}
        .plano-sub {{ color: {PALETTE["muted"]}; font-size: 13px; }}
        .plano-badges {{ margin-top: 14px; }}
        .badge {{
            display: inline-block; border-radius: 20px; padding: 4px 12px;
            font-size: 12px; margin-right: 8px; margin-bottom: 8px;
        }}
        /* Section header */
        .section-header {{
            display: inline-block; background: #ffffff10; border: 1px solid {PALETTE["border"]};
            border-radius: 8px; padding: 6px 14px; font-size: 12px; color: {PALETTE["muted"]};
            letter-spacing: 1.5px; text-transform: uppercase; margin: 20px 0 4px;
        }}
        .section-sub {{ color: {PALETTE["muted"]}; font-size: 12px; margin-bottom: 14px; }}
        /* Cards */
        .card {{
            background: {PALETTE["card"]}; border: 1px solid {PALETTE["border"]};
            border-radius: 14px; padding: 18px 20px; margin-bottom: 16px;
        }}
        .card-title {{ font-weight: 700; font-size: 15px; margin-bottom: 10px; }}
        .card ul {{ margin: 0; padding-left: 18px; }}
        .card li {{ font-size: 13.5px; margin-bottom: 7px; line-height: 1.6; color: {PALETTE["text"]}; }}
        .meta {{ font-size: 12px; color: {PALETTE["muted"]}; margin-bottom: 10px; }}
        .quote-block {{
            font-style: italic; font-size: 15px; line-height: 1.7; padding-left: 14px;
            margin-bottom: 14px;
        }}
        .callout {{
            border-radius: 12px; padding: 14px 16px; font-size: 13px; margin-top: 14px;
        }}
        /* Expander tweaks */
        details {{
            background: {PALETTE["card"]} !important;
            border: 1px solid {PALETTE["border"]} !important;
            border-radius: 14px !important;
        }}
        summary {{ font-size: 14px !important; }}
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{ gap: 4px; }}
        .stTabs [data-baseweb="tab"] {{ color: {PALETTE["muted"]}; }}
        .stTabs [aria-selected="true"] {{ color: {PALETTE["text"]} !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────────────────────
# HELPERS DE RENDERIZAÇÃO
# ──────────────────────────────────────────────────────────────────────────
def render_header():
    badges_html = "".join(
        f'<span class="badge" style="background:{cor}18;border:1px solid {cor}44;color:{cor};">🎤 {label}</span>'
        for cor, label in LEGENDA_ANCORAS
    )
    badges_html += (
        f'<span class="badge" style="background:#ffffff0f;border:1px solid {PALETTE["border"]};'
        f'color:{PALETTE["muted"]};">📐 Sala em formato U</span>'
    )
    st.markdown(
        f"""
        <div class="plano-header">
            <div class="plano-eyebrow">Plano de Aula</div>
            <div class="plano-title">Entre Emoções<br/>e Escolhas</div>
            <div class="plano-sub">Palestra Participativa · 2 aulas de 55 min · Faixa etária: 14–16 anos</div>
            <div class="plano-sub" style="margin-top:2px;">Palestrantes: Miguel &amp; Maria Clara · Mediação: Professora</div>
            <div class="plano-badges">{badges_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_block(block: dict):
    color = anchor_color(block["anchor"])
    with st.expander(f'{block["num"]} · {block["title"]}'):
        st.markdown(
            f'<div class="meta">⏱ {block["time"]} &nbsp;·&nbsp; '
            f'<span style="color:{color};">🎤 {block["anchor"]}</span></div>',
            unsafe_allow_html=True,
        )
        items = "".join(f"<li>{c}</li>" for c in block["content"])
        st.markdown(f"<ul>{items}</ul>", unsafe_allow_html=True)


def render_section_header(label: str, sublabel: str = "", total: str = ""):
    total_html = f'<span style="float:right;color:{PALETTE["muted"]};font-size:12px;">{total}</span>' if total else ""
    st.markdown(
        f'<div class="section-header">{label}</div>{total_html}',
        unsafe_allow_html=True,
    )
    if sublabel:
        st.markdown(f'<div class="section-sub">{sublabel}</div>', unsafe_allow_html=True)


def render_faq(item: dict):
    with st.expander(f'❓ {item["question"]}'):
        items = "".join(f"<li>{a}</li>" for a in item["answer"])
        st.markdown(f"<ul>{items}</ul>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="font-size:12px;color:{PALETTE["muted"]};margin-top:6px;">'
            f'↳ Conecta com: {item["link"]}</div>',
            unsafe_allow_html=True,
        )


# ──────────────────────────────────────────────────────────────────────────
# LAYOUT PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────
render_header()

tab_estrutura, tab_divisao, tab_citacoes, tab_faq, tab_dicas, tab_evitar = st.tabs(
    ["Estrutura", "Divisão de Falas", "Citações", "Perguntas Frequentes", "Dicas", "O que Evitar"]
)

# --- Estrutura -----------------------------------------------------------
with tab_estrutura:
    render_section_header(
        "1ª Aula — 55 min",
        "Abertura, três citações e a base teórica dos Quatro Amores",
        "≈ 55 min",
    )
    for b in AULA1:
        render_block(b)

    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:12px;margin:20px 0;padding:12px 18px;
        background:#ffffff07;border-radius:10px;border:1px dashed {PALETTE["border"]};">
            <span style="font-size:22px;">☕</span>
            <div>
                <div style="font-weight:700;font-size:13px;">Intervalo</div>
                <div style="font-size:12px;color:{PALETTE["muted"]};">Entre as duas aulas</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_section_header(
        "2ª Aula — 55 min",
        "Aprofundamento emocional, dinâmicas em grupo e reflexão final",
        "≈ 55 min",
    )
    for b in AULA2:
        render_block(b)

    st.markdown(
        f"""
        <div class="callout" style="background:{PALETTE["accent2"]}11;border:1px solid {PALETTE["accent2"]}33;color:{PALETTE["muted"]};">
            ⚠️ Os tempos são estimativas. O debate das citações (bloco 02) pode ser encurtado se houver atraso.
            A sala em U deve ser organizada antes da palestra começar.
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Divisão de Falas ------------------------------------------------------
with tab_divisao:
    st.markdown(
        f'<p style="color:{PALETTE["muted"]};font-size:13px;margin-bottom:20px;">'
        "Dois palestrantes conduzem a conversa, e a professora entra em três momentos-chave: "
        "abertura, fechamento da 1ª aula e encerramento final.</p>",
        unsafe_allow_html=True,
    )
    for p in DIVISAO:
        blocks_html = "".join(
            f'<div style="display:flex;gap:10px;margin-bottom:8px;font-size:13.5px;">'
            f'<span style="color:{p["color"]};">›</span> {b}</div>'
            for b in p["blocks"]
        )
        st.markdown(
            f"""
            <div class="card" style="border-color:{p["color"]}44;">
                <div class="card-title" style="color:{p["color"]};">🎤 {p["name"]}</div>
                {blocks_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

# --- Citações ---------------------------------------------------------------
with tab_citacoes:
    st.markdown(
        f'<p style="color:{PALETTE["muted"]};font-size:13px;margin-bottom:20px;">'
        "As três citações abrem a palestra como provocação — não há resposta certa. "
        "O objetivo é mostrar que visões opostas (e uma terceira, intermediária) sobre amor "
        "podem ser igualmente válidas.</p>",
        unsafe_allow_html=True,
    )
    for c in CITACOES:
        analise_html = "".join(
            f'<div style="display:flex;gap:10px;margin-bottom:7px;font-size:13px;">'
            f'<span style="color:{c["color"]};">›</span> {a}</div>'
            for a in c["analise"]
        )
        st.markdown(
            f"""
            <div class="card" style="border-color:{c["color"]}44;">
                <div class="card-title" style="color:{c["color"]};">{c["author"]}</div>
                <div class="quote-block" style="border-left:3px solid {c["color"]};">"{c["quote"]}"</div>
                <div style="font-size:12px;color:{PALETTE["muted"]};margin-bottom:8px;text-transform:uppercase;letter-spacing:1px;">
                    Como usar na palestra
                </div>
                {analise_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    amores_html = "".join(
        f'<div style="display:flex;gap:10px;margin-bottom:7px;font-size:13px;">'
        f'<span style="color:{PALETTE["teal"]};font-weight:700;min-width:60px;">{nome}</span> {desc}</div>'
        for nome, desc in QUATRO_AMORES
    )
    st.markdown(
        f"""
        <div class="card" style="background:{PALETTE["teal"]}11;border-color:{PALETTE["teal"]}33;">
            <div class="card-title" style="color:{PALETTE["teal"]};">📖 Os Quatro Amores, em resumo (bloco 04)</div>
            {amores_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="callout" style="background:{PALETTE["green"]}11;border:1px solid {PALETTE["green"]}33;">
            <strong style="color:{PALETTE["green"]};">💡 Dica de ouro:</strong>
            Não expliquem as citações antes de perguntar. Deixem a turma interpretar primeiro —
            as respostas deles são o melhor ponto de partida.
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Perguntas Frequentes ----------------------------------------------------
with tab_faq:
    st.markdown(
        f'<p style="color:{PALETTE["muted"]};font-size:13px;margin-bottom:20px;">'
        "Perguntas que costumam surgir espontaneamente — ou que podem ser usadas para reaquecer "
        "a turma se o debate esfriar. Cada uma indica em qual bloco ela se encaixa melhor.</p>",
        unsafe_allow_html=True,
    )
    for q in FAQ:
        render_faq(q)

# --- Dicas --------------------------------------------------------------------
with tab_dicas:
    st.markdown(
        f'<p style="color:{PALETTE["muted"]};font-size:13px;margin-bottom:20px;">'
        'O diferencial não vai ser "falar sobre namoro" — vai ser tratar adolescentes com '
        "maturidade e fazê-los refletir.</p>",
        unsafe_allow_html=True,
    )
    for icon, text in DICAS:
        st.markdown(
            f"""
            <div style="display:flex;gap:14px;align-items:flex-start;background:{PALETTE["card"]};
            border:1px solid {PALETTE["border"]};border-radius:12px;padding:14px 16px;margin-bottom:10px;">
                <span style="font-size:22px;">{icon}</span>
                <span style="font-size:13.5px;line-height:1.6;">{text}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

# --- O que Evitar ---------------------------------------------------------------
with tab_evitar:
    st.markdown(
        f'<p style="color:{PALETTE["muted"]};font-size:13px;margin-bottom:20px;">'
        "Essenciais para que a palestra não perca credibilidade ou vire bagunça.</p>",
        unsafe_allow_html=True,
    )
    for a in AVOID:
        st.markdown(
            f"""
            <div style="display:flex;gap:14px;align-items:center;background:{PALETTE["card"]};
            border:1px solid #e8445a22;border-radius:12px;padding:13px 16px;margin-bottom:10px;">
                <span style="font-size:18px;color:{PALETTE["accent"]};">✕</span>
                <span style="font-size:13.5px;">{a}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )