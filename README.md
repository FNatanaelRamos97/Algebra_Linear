# Algebra_Linear

### Fluxograma do código

```mermaid
flowchart TD
    A([Início]) --> B[/Informar a ordem da matriz n/]
    B --> C{n >= 3?}

    C -- Não --> D[Solicitar novamente a ordem]
    D --> B

    C -- Sim --> E[Inicializar matriz aumentada]
    E --> F[/Ler coeficientes e termos independentes/]
    F --> G[Exibir matriz aumentada inicial]

    G --> H[Iniciar eliminação de Gauss]
    H --> I[Selecionar o maior pivô em módulo]
    I --> J[Trocar linhas se necessário]
    J --> K{Pivô é zero?}

    K -- Sim --> N[Avançar para próxima coluna]
    K -- Não --> L[Calcular fator de eliminação]
    L --> M[Zerar elementos abaixo do pivô]
    M --> N

    N --> O{Existem mais pivôs?}
    O -- Sim --> I
    O -- Não --> P[Exibir matriz triangular superior]

    P --> Q[Calcular posto da matriz A e da matriz aumentada]
    Q --> R{Posto A é diferente do posto aumentada?}

    R -- Sim --> S[Classificar como SI]
    S --> T[Informar: sistema sem solução]

    R -- Não --> U{Posto A é igual a n?}

    U -- Sim --> V[Classificar como SPD]
    V --> W[Realizar retrosubstituição]
    W --> X[Exibir solução única]

    U -- Não --> Y[Classificar como SPI]
    Y --> Z[Informar: infinitas soluções]

    T --> FIM([Fim])
    X --> FIM
    Z --> FIM

    style A fill:#d5f5e3,stroke:#229954
    style FIM fill:#d5f5e3,stroke:#229954
    style S fill:#fadbd8,stroke:#c0392b
    style V fill:#d6eaf8,stroke:#2874a6
    style Y fill:#fcf3cf,stroke:#b7950b
``