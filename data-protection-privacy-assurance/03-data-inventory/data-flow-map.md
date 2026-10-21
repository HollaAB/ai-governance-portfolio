# Data-Flow Map

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

How personal data moves between people, the Club's systems and its processors. Activity IDs refer to the [personal data inventory](personal-data-inventory.csv).

## Members and bookings (PA-01 to PA-05)

```mermaid
flowchart LR
    M[Member] -->|application, app| FW[FairwayOne<br>club management system<br>hosted in South Africa]
    M -->|WhatsApp, app| KA[Kijani Assist<br>Sauti AI Labs]
    KA -->|prompts, no account data stored| MC[ModelCo<br>language model<br>outside Kenya]
    KA -->|bookings, verified balance queries| FW
    POS[Point of sale] -->|charges| FW
    FW -->|payments| PAY[Bank and mobile money<br>separate controllers]
    FW -->|handicaps| GU[National golf union]
    FW -->|opted-in contacts| EV[Events partner]
```

## Gate and site security (PA-06 to PA-08)

```mermaid
flowchart LR
    V[Vehicle at gate] --> ANPR[ANPR camera]
    ANPR -->|plate matches an opted-in member| G[Gate opens]
    ANPR -->|no match| GD[Guard checks manually<br>visitor register]
    CAM[64 CCTV cameras] --> NVR[On-site recorder<br>30-day retention]
    NVR -->|viewing only, logged| LG[Linda Guard Services]
    GD --> VR[Visitor register]
```

## Staff (PA-09 to PA-12)

```mermaid
flowchart LR
    E[Employee] --> HR[HR files]
    HR --> PB[Payroll bureau]
    PB --> KRA[KRA]
    PB --> SS[NSSF and SHIF]
    C[Caddie] --> CR[Caddie register] --> MM[M-Pesa payments]
```

## Transfers outside Kenya

| Flow | Destination | Safeguard | Assessment |
|---|---|---|---|
| Member records to FairwayOne | South Africa | Data processing agreement with transfer clauses, signed 10 December 2026 | [cross-border-transfer-assessment.md](../05-processors/cross-border-transfer-assessment.md) |
| Chatbot prompts to ModelCo | Outside Kenya | Sauti AI Labs agreement covering ModelCo; no account data sent to ModelCo | Same document |
