from fastapi import APIRouter
from openai import OpenAI


from app.config import settings
from app.schemas.ai import UserAIRequest

router = APIRouter()

clientOpenAI = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


@router.post("/ai")
def ai(request: UserAIRequest):

    user_chat = request.messages
    user_papers = request.papers
    
    user_chat = [{"role": msg.role, "content": msg.content} for msg in request.messages]
    user_papers = [{"title": paper.title, "authors": paper.authors, "abstract": paper.abstract, "published": paper.published, "updated": paper.updated, "pdf_url": paper.pdf_url, "entry_id": paper.entry_id, "categories": paper.categories} for paper in request.papers]

    array = [
    {
      "title": "Quantum Cryptography for Enhanced Network Security: A Comprehensive Survey of Research, Developments, and Future Directions",
      "authors": [
        "Mst Shapna Akter"
      ],
      "abstract": "With the ever-growing concern for internet security, the field of quantum\ncryptography emerges as a promising solution for enhancing the security of\nnetworking systems. In this paper, 20 notable papers from leading conferences\nand journals are reviewed and categorized based on their focus on various\naspects of quantum cryptography, including key distribution, quantum bit\ncommitment, post quantum cryptography, and counterfactual quantum key\ndistribution. The paper explores the motivations and challenges of employing\nquantum cryptography, addressing security and privacy concerns along with\nexisting solutions. Secure key distribution, a critical component in ensuring\nthe confidentiality and integrity of transmitted information over a network, is\nemphasized in the discussion. The survey examines the potential of quantum\ncryptography to enable secure key exchange between parties, even when faced\nwith eavesdropping, and other applications of quantum cryptography.\nAdditionally, the paper analyzes the methodologies, findings, and limitations\nof each reviewed study, pinpointing trends such as the increasing focus on\npractical implementation of quantum cryptography protocols and the growing\ninterest in postquantum cryptography research. Furthermore, the survey\nidentifies challenges and open research questions, including the need for more\nefficient quantum repeater networks, improved security proofs for continuous\nvariable quantum key distribution, and the development of quantum resistant\ncryptographic algorithms.",
      "published": "2023-06-02",
      "updated": "2023-06-02",
      "pdf_url": "http://arxiv.org/pdf/2306.09248v1",
      "entry_id": "http://arxiv.org/abs/2306.09248v1",
      "categories": "cs.CR"
    },
    {
      "title": "Quantum-Resistant Cryptography",
      "authors": [
        "John Preuß Mattsson",
        "Ben Smeets",
        "Erik Thormarker"
      ],
      "abstract": "Quantum-resistant cryptography is cryptography that aims to deliver\ncryptographic functions and protocols that remain secure even if large-scale\nfault-tolerant quantum computers are built. NIST will soon announce the first\nselected public-key cryptography algorithms in its Post-Quantum Cryptography\n(PQC) standardization which is the most important current effort in the field\nof quantum-resistant cryptography. This report provides an overview to security\nexperts who do not yet have a deep understanding of quantum-resistant\ncryptography. It surveys the computational model of quantum computers; the\nquantum algorithms that affect cryptography the most; the risk of\nCryptographically Relevant Quantum Computers (CRQCs) being built; the security\nof symmetric and public-key cryptography in the presence of CRQCs; the NIST PQC\nstandardization effort; the migration to quantum-resistant public-key\ncryptography; the relevance of Quantum Key Distribution as a complement to\nconventional cryptography; and the relevance of Quantum Random Number\nGenerators as a complement to current hardware Random Number Generators.",
      "published": "2021-12-01",
      "updated": "2021-12-01",
      "pdf_url": "http://arxiv.org/pdf/2112.00399v1",
      "entry_id": "http://arxiv.org/abs/2112.00399v1",
      "categories": "cs.CR"
    },
    {
      "title": "Unconditionally secure key distribution without quantum channel",
      "authors": [
        "Hua-Lei Yin"
      ],
      "abstract": "Key distribution plays a fundamental role in cryptography. Currently, the\nquantum scheme stands as the only known method for achieving unconditionally\nsecure key distribution. This method has been demonstrated over distances of\n508 and 1002 kilometers in the measurement-device-independent and twin-field\nconfigurations, respectively. However, quantum key distribution faces\ntransmission distance issues and numerous side channel attacks since the basic\nphysical picture requires the use of quantum channels between users. Even when\nquantum repeater and quantum constellation are used, commercializing quantum\ncryptography on a large scale remains unattainable due to the considerable\nexpense and significant technical hurdles associated with establishing a global\nquantum network and facilitating mobile quantum communication. Here, by\ndiscovering the provable quantum one-way function, we propose another key\ndistribution scheme with unconditional security, named probability key\ndistribution, that promises users between any two distances to generate a fixed\nand high secret key rate. There are no quantum channels for exchanging quantum\nsignals between two legitimate users. Non-local entangled states can be\ngenerated, identified and measured in the equivalent virtual protocol and can\nbe used to extract secret keys. We anticipate that this discovery presents a\nparadigm shift in achieving unconditionally secure cryptography, thereby\nfacilitating its widespread application on a global scale.",
      "published": "2024-08-24",
      "updated": "2024-08-24",
      "pdf_url": "http://arxiv.org/pdf/2408.13602v1",
      "entry_id": "http://arxiv.org/abs/2408.13602v1",
      "categories": "quant-ph"
    },
    {
      "title": "A deep learning based known plaintext attack method for chaotic cryptosystem",
      "authors": [
        "Fusen Wang",
        "Jun Sang",
        "Qi Liu",
        "Chunlin Huang",
        "Jinghan Tan"
      ],
      "abstract": "In this paper, we propose a known-plaintext attack (KPA) method based on deep\nlearning for traditional chaotic encryption scheme. We employ the convolutional\nneural network to learn the operation mechanism of chaotic cryptosystem, and\naccept the trained network as the final decryption system. To evaluate the\nattack performance of different networks on different chaotic cryptosystem, we\nadopt two neural networks to perform known-plaintext attacks on two distinct\nchaotic encryption schemes. The experimental results demonstrate the potential\nof deep learning-based method for known-plaintext attack against chaotic\ncryptosystem. Different from the previous known-plaintext attack methods, which\nwere usually limited to a specific chaotic cryptosystem, a neural network can\nbe applied to the cryptanalysis of various chaotic cryptosystems with deep\nlearning-based approach, while several different networks can be designed for\nthe cryptanalysis of chaotic cryptosystems. This paper provides a new idea for\nthe cryptanalysis of chaotic image encryption algorithm.",
      "published": "2021-03-09",
      "updated": "2021-03-09",
      "pdf_url": "http://arxiv.org/pdf/2103.05242v1",
      "entry_id": "http://arxiv.org/abs/2103.05242v1",
      "categories": "cs.CR"
    },
    {
      "title": "Cryptanalysis of a novel cryptosystem based on chaotic oscillators and feedback inversion",
      "authors": [
        "G. Alvarez",
        "L. Hernandez",
        "F. Montoya",
        "J. Munoz"
      ],
      "abstract": "An analysis of a recently proposed cryptosystem based on chaotic oscillators\nand feedback inversion is presented. It is shown how the cryptosystem can be\nbroken when Duffing's oscillator is considered. Some implementation problems of\nthe system are also discussed.",
      "published": "2003-11-20",
      "updated": "2003-11-20",
      "pdf_url": "http://arxiv.org/pdf/nlin/0311042v1",
      "entry_id": "http://arxiv.org/abs/nlin/0311042v1",
      "categories": "nlin.CD"
    },
    {
      "title": "Quantum impossible differential and truncated differential cryptanalysis",
      "authors": [
        "Huiqin Xie",
        "Li Yang"
      ],
      "abstract": "Traditional cryptography is suffering a huge threat from the development of\nquantum computing. While many currently used public-key cryptosystems would be\nbroken by Shor's algorithm, the effect of quantum computing on symmetric ones\nis still unclear. The security of symmetric ciphers relies heavily on the\ndevelopment of cryptanalytic tools. Thus, in order to accurately evaluate the\nsecurity of symmetric primitives in the post-quantum world, it is significant\nto improve classical cryptanalytic methods using quantum algorithms. In this\npaper, we focus on two variants of differential cryptanalysis: truncated\ndifferential cryptanalysis and impossible differential cryptanalysis. Based on\nthe fact that Bernstein-Vazirani algorithm can be used to find the linear\nstructures of Boolean functions, we propose two quantum algorithms that can be\nused to find high-probability truncated differentials and impossible\ndifferentials of block ciphers, respectively. We rigorously prove the validity\nof the algorithms and analyze their complexity. Our algorithms treat all rounds\nof the reduced cipher as a whole and only concerns the input and output\ndifferences at its both ends, instead of specific differential characteristics.\nTherefore, to a certain extent, they alleviate the weakness of conventional\ndifferential cryptanalysis, namely the difficulties in finding differential\ncharacteristics as the number of rounds increases.",
      "published": "2017-12-18",
      "updated": "2018-07-23",
      "pdf_url": "http://arxiv.org/pdf/1712.06997v2",
      "entry_id": "http://arxiv.org/abs/1712.06997v2",
      "categories": "quant-ph"
    },
    {
      "title": "Post-Quantum Cryptographic Hardware Primitives",
      "authors": [
        "Lake Bu",
        "Rashmi Agrawal",
        "Hai Cheng",
        "Michel A. Kinsy"
      ],
      "abstract": "The development and implementation of post-quantum cryptosystems have become\na pressing issue in the design of secure computing systems, as general quantum\ncomputers have become more feasible in the last two years. In this work, we\nintroduce a set of hardware post-quantum cryptographic primitives (PCPs)\nconsisting of four frequently used security components, i.e., public-key\ncryptosystem (PKC), key exchange (KEX), oblivious transfer (OT), and\nzero-knowledge proof (ZKP). In addition, we design a high speed polynomial\nmultiplier to accelerate these primitives. These primitives will aid\nresearchers and designers in constructing quantum-proof secure computing\nsystems in the post-quantum era.",
      "published": "2019-03-09",
      "updated": "2019-03-09",
      "pdf_url": "http://arxiv.org/pdf/1903.03735v1",
      "entry_id": "http://arxiv.org/abs/1903.03735v1",
      "categories": "cs.CR"
    },
    {
      "title": "Physical cryptographic primitives by chemical vapor deposition of layered MoS2",
      "authors": [
        "Abdullah Alharbi",
        "Darren Armstrong",
        "Somayah Alharbi",
        "Davood Shahrjerdi"
      ],
      "abstract": "Development of physical cryptographic primitives for generating strong\nsecurity keys is central to combating security threats such as counterfeiting\nand unauthorized access to electronic devices. We introduce a new class of\nphysical cryptographic primitives from layered molybdenum disulfide (MoS2)\nwhich leverages the unique properties of this material system. Using chemical\nvapor deposition, we synthesize a MoS2 monolayer film covered with speckles of\nmultilayer islands, where the growth process is engineered for an optimal\nspeckle density. The physical cryptographic primitive is an array of 2048\npixels fabricated from this film. Using the Clark-Evans test, we confirm that\nthe distribution of islands on the film exhibits complete spatial randomness,\nmaking this cryptographic primitive ideal for security applications. A unique\noptical response is generated by applying an optical stimulus to the structure.\nThe basis for this unique response is the dependence of the photoemission on\nthe number of MoS2 layers which by design is random throughout the film. The\noptical response is used to generate cryptographic keys. Standard security\ntests confirm the uniqueness, reliability, and uniformity of these keys. This\nstudy reveals a new opportunity for generating strong and versatile\nnano-engineered security primitives from layered transition metal\ndichalcogenides.",
      "published": "2017-06-21",
      "updated": "2017-06-21",
      "pdf_url": "http://arxiv.org/pdf/1706.06745v1",
      "entry_id": "http://arxiv.org/abs/1706.06745v1",
      "categories": "cond-mat.mtrl-sci"
    },
    {
      "title": "Point Intervention: Improving ACVP Test Vector Generation Through Human Assisted Fuzzing",
      "authors": [
        "Iaroslav Gridin",
        "Antonis Michalas"
      ],
      "abstract": "Automated Cryptographic Validation Protocol (ACVP) is an existing protocol\nthat is used to validate a software or hardware cryptographic module\nautomatically. In this work, we present a system providing the method and tools\nto produce well-covering tests in ACVP format for cryptographic libraries. The\nsystem achieves better coverage than existing fuzzing methods by using a hybrid\napproach to fuzzing cryptographic primitives. In addition, the system offers a\nframework that allows to creates easily and securely create testing modules for\ncryptographic libraries. The work demonstrates how this system has been used to\nimprove automated testing of NSS (Network Security Services), a popular\ncryptographic library, detect its vulnerabilities and suggest ways to improve\nand further develop the ACVP test format.",
      "published": "2024-07-11",
      "updated": "2024-07-11",
      "pdf_url": "http://arxiv.org/pdf/2407.08535v1",
      "entry_id": "http://arxiv.org/abs/2407.08535v1",
      "categories": "cs.CR"
    }
  ]

    promt_inicial = """
    Eres un asistente experto en redacción académica e investigación. Tu objetivo es ayudar a mejorar la calidad de un artículo científico proporcionando sugerencias bien fundamentadas basadas en los abstracts y títulos de otros trabajos de investigación. Tienes acceso a los siguientes abstracts con sus respectivos títulos, que representan el estado del arte en el campo:

    {array}

    El usuario proporcionará una sección específica de su artículo científico en latex (por ejemplo, Introducción, Metodología, Resultados, Discusión, o Conclusiones) junto con una solicitud detallada. Tu tarea es:

    1. Leer y entender el contenido proporcionado por el usuario.
    2. Analizar cómo puede mejorar esa sección, ya sea en términos de claridad, profundidad, estructura o relevancia.
    3. Utilizar los abstracts y títulos proporcionados para sugerir referencias, ideas adicionales o argumentos que enriquezcan el contenido.
    4. Proponer un texto reescrito o modificado, siguiendo las indicaciones del usuario y respetando el tono y estilo académico.

    Todas las sugerencias y mejoras deben ser claras, bien justificadas y alineadas con las prácticas de escritura académica. Si detectas algún problema en la coherencia, gramática o formato del texto proporcionado, también indícalo y sugiere correcciones incluyendo solo los cambios del latex y la explicación.

    ¿Entendido? Comencemos.
    """
    messages = [
    {
        "role": "system", "content": promt_inicial
    }
    ]

    for message in user_chat:
        messages.append({"role": message["role"], "content": message["content"]})

    try:
        response = clientOpenAI.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        
        return response.choices[0].message
    except Exception as e:
        return str(e)

