# Generated by Django 2.1.7 on 2019-05-30 14:07
# Edited by Francis Normand to upload the background markdown content for the sample test

from django.db import migrations


def upload_background_markdown(apps, schema_editor):
    # get models
    language = apps.get_model("custom_models", "Language")
    item_type = apps.get_model("custom_models", "ItemType")
    item = apps.get_model("custom_models", "Item")
    item_text = apps.get_model("custom_models", "ItemText")
    test = apps.get_model("custom_models", "Test")

    # get db alias
    db_alias = schema_editor.connection.alias

    # lookup languages; do not use bulk_create since we need these objects later on
    l_english = (
        language.objects.using(db_alias)
        .filter(ISO_Code_1="en", ISO_Code_2="en-ca")
        .last()
    )
    l_french = (
        language.objects.using(db_alias)
        .filter(ISO_Code_1="fr", ISO_Code_2="fr-ca")
        .last()
    )
    emib_sample_item_id = (
        test.objects.using(db_alias).filter(test_name="emibSampleTest").last().item_id
    )

    # create item_types; do not use bulk_create since we need these objects later on
    it_background = item_type(type_desc="background")
    it_background.save()
    it_markdown = item_type(type_desc="markdown")
    it_markdown.save()

    # create items; do not use bulk_create since we need these objects later on
    # background
    i_background = item(
        parent_id=emib_sample_item_id, item_type_id=it_background, order=0
    )
    i_background.save()

    # background information item
    i_background_info = item(parent_id=i_background, item_type_id=it_markdown, order=1)
    i_background_info.save()

    # organizational information item
    i_organizational_info = item(
        parent_id=i_background, item_type_id=it_markdown, order=2
    )
    i_organizational_info.save()

    # organizational structure item
    i_organizational_structure = item(
        parent_id=i_background, item_type_id=it_markdown, order=3
    )
    i_organizational_structure.save()

    # team information (1) item
    i_team_information_1 = item(
        parent_id=i_background, item_type_id=it_markdown, order=4
    )
    i_team_information_1.save()

    # team information (2) item
    i_team_information_2 = item(
        parent_id=i_background, item_type_id=it_markdown, order=5
    )
    i_team_information_2.save()

    # bulk create item_text
    item_text.objects.using(db_alias).bulk_create(
        [
            item_text(
                item_id=i_background, text_detail="Background", language=l_english
            ),
            item_text(item_id=i_background, text_detail="Contexte", language=l_french),
            item_text(
                item_id=i_background_info,
                text_detail="""## Background Information

In this exercise, you are assuming the role of Claude Huard, the new manager of the Quality Assurance (QA) team. You are replacing Gary Severna, who recently retired. Your team is a part of the Services and Communications (SC) unit of a public service organisation called the Organizational Development Council (ODC). It is now 9:30 a.m. on Monday, November 7th.

In the following sections, you will find information about ODC and the QA Team. You will be able to access it throughout the test.
""",
                language=l_english,
            ),
            item_text(
                item_id=i_background_info,
                text_detail="""## Contexte

Dans cet exercice, vous jouez le rôle de Claude Huard, le nouveau gestionnaire de l’Équipe de l’assurance de la qualité (AQ). Vous remplacez Gary Severna, qui a récemment pris sa retraite. Votre équipe fait partie de l’Unité des services et communications (SC) d’un organisme de la fonction publique appelé Conseil du développement organisationnel (CDO). Il est 9 h 30 le lundi 7 novembre.

Dans les sections suivantes, vous trouverez de l’information sur le CDO et l’Équipe d’AQ. Vous serez en mesure d’y accéder tout au long du test.
""",
                language=l_french,
            ),
            item_text(
                item_id=i_organizational_info,
                text_detail="""## Information about the Organizational Development Council (ODC)

The ODC is an independent government agency that promotes organizational development across the public service. The ODC’s mandate is to provide training to all public service employees to maintain a productive and commendable workforce. The organization is responsible for: (1) the creation and evaluation of training programs; (2) research and innovation in learning, transfer of training, and technology; and (3) conducting audits on workplace behaviors in adherence to the ethical and professional standards of public service. With its headquarters located in the National Capital Region, the ODC currently employs approximately 100 individuals.

### Priorities

- To ensure that the organization continues to enhance productive workplace behaviors through policies of ethical and professional conduct.
- To continuously evaluate the effectiveness and utility of training programs across the public service.
- To deliver high-quality training programs across the public service, supporting the Government of Canada’s priorities.
- To manage the documentation and communication of client training activities.

### Risks

- The scope and complexity of training programs pose ongoing challenges for (1) their timely delivery and effectiveness in responding to new and emerging policy priorities; (2) maintaining partnerships that are essential for high-quality training program development, delivery, and evaluation; (3) keeping pace with the evolving demands of clients and with new learning technology.
""",
                language=l_english,
            ),
            item_text(
                item_id=i_organizational_info,
                text_detail="""## Renseignements sur le Conseil du Développement Organisationnel (CDO)

Le CDO est un organisme gouvernemental indépendant qui œuvre à la promotion du développement organisationnel au sein de la fonction publique. Le mandat du CDO est d’offrir de la formation à tous les employés de la fonction publique afin de maintenir une main-d’œuvre productive et digne d’éloges. L’organisme est responsable de : (1) la création et l’évaluation des programmes de formation; (2) la recherche et l’innovation dans les domaines de l’apprentissage, du transfert de formation et de la technologie; (3) la réalisation de vérifications en matière de comportements en milieu de travail, conformément aux normes d’éthique et de conduite professionnelle de la fonction publique. Le CDO, dont l’administration centrale est située dans la région de la capitale nationale, compte actuellement environ 100 employés.

### Priorités

- Veiller à ce que l’organisme continue d’améliorer les comportements productifs au travail par la mise en place de politiques en matière de comportement éthique et professionnel.
- Évaluer de façon continue l’efficacité et l’utilité des programmes de formation au sein de la fonction publique.
- Offrir à l’échelle de la fonction publique des programmes de qualité supérieure qui appuient les priorités du gouvernement du Canada.
- Gérer la documentation et la communication des activités de formation des clients.

### Risques

- La portée et la complexité des programmes de formation posent des défis continuels quant à : (1) leur livraison dans les délais prévus et leur efficacité à répondre aux priorités stratégiques nouvelles ou émergentes; (2) le maintien de partenariats essentiels à l’élaboration, à la livraison et à l’évaluation de programmes de formation de haute qualité; (3) la capacité de suivre le rythme des demandes changeantes des clients et la nouvelle technologie d’apprentissage.
""",
                language=l_french,
            ),
            item_text(
                item_id=i_organizational_structure,
                text_detail="""## Organizational Structure

The ODC has an organizational structure consisting of four units including: Corporate Affairs, Research and Innovations, Training Program Development, and Services and Communications.

**Corporate affairs (CA).** The CA unit is comprised of the Human Resources Team, the Finance Team and the Information Technology Team. Together these teams are responsible for the management of the workforce, the work environment, the finances, as well as the technology and information in ODC.

**Research and innovations (RI).** The main goals of the RI unit are to conduct research initiatives in learning, transfer of training, and technology and to help develop innovative teaching techniques that promote employee productivity and general well-being.

**Program development (PD).** The focus of the PD unit is to plan, develop and administer training programs across the public service. To do so, the unit establishes and maintains relationships with clients and partners, and conducts analyses of their organizational development training needs.

**Services and communications (SC).** The main goals of the SC unit are to continuously evaluate training programs offered by organizations in the public service, conduct internal and external audits for partners and clients, and oversee the dissemination of information (e.g., content review for online tools, developing documentation for training programs). The SC unit is comprised of the Quality Assurance Team, the Service and support Team, the Audits Team, and the E-Training Team.
""",
                language=l_english,
            ),
            item_text(
                item_id=i_organizational_structure,
                text_detail="""## Structure organisationnelle

Le CDO a une structure organisationnelle qui comporte les quatre unités suivantes : Affaires ministérielles, Recherche et innovations, Développement de programmes, et Services et communications.

**Affaires ministérielles (AM).** L’Unité des AM est composée de l’Équipe des ressources humaines, l’Équipe des finances et l’Équipe de la technologie de l’information. Ensemble, ces équipes sont responsables de la gestion de la main-d’œuvre, de l’environnement de travail, des finances, ainsi que de la technologie et de l’information à l’intérieur du CDO.

**Recherche et innovations (RI).** Les principaux objectifs de l’Unité de RI sont de mener des initiatives de recherche en apprentissage, en transfert de formation et en technologie; et de contribuer à l’élaboration de techniques d’enseignement novatrices, afin de promouvoir la productivité et le bien-être général des employés.

**Développement de programmes (DP).** L’Unité du DP vise à planifier, à créer et à administrer les programmes de formation au sein de la fonction publique. Pour ce faire, l’unité établit et entretient des relations avec les clients et les partenaires, et analyse leurs besoins de formation en développement organisationnel.

**Services et communications (SC).** Les principaux objectifs de l’Unité des SC sont d’évaluer de façon continue les programmes de formation offerts par les organisations de la fonction publique, effectuer des vérifications internes et externes pour les partenaires et les clients, et surveiller la diffusion de l’information (p. ex., évaluer le contenu des outils en ligne, rédiger les documents relatifs aux programmes de formation). L’Unité des SC est composée de l’Équipe de l’assurance de la qualité, l’Équipe du service et soutien, l’Équipe des vérifications et de l’Équipe des formations en ligne.
""",
                language=l_french,
            ),
            item_text(
                item_id=i_team_information_1,
                text_detail="""## Information about the Quality Assurance (QA) Team

### Team Members

#### Director: Nancy Ward

Your Director is Nancy Ward. The director of the Services and Communications unit applies policies and oversees the creation, delivery, and evaluation of training programs and audits. The director is also responsible for overseeing all internal and external communication channels including web content.

#### Manager: Claude Huard (you)

Your role as manager of the Quality Assurance Team is to oversee the content review and make final recommendations for training manuals, specifications, and other related training documents. The role also involves making staffing recommendations, managing the performance of team members, as well as coordinating the sharing of information and expertise with partners and stakeholders. The manager is also responsible for ensuring compliance to policy and professional standards and for delivering executive reports that include project updates, timelines, and budgetary implications.

#### Quality Assurance Analysts

The members of your team are Danny McBride, Serge Duplessis, Marina Richter, Mary Woodside, Charlie Wang, and Jack Laurier. All team members are Quality Assurance Analysts and, as such, are experts in documentation and make recommendations on training documents and online content.
""",
                language=l_english,
            ),
            item_text(
                item_id=i_team_information_1,
                text_detail="""## Information sur l’Équipe de l’assurance de la qualité (AQ)

### Membres de l’équipe

#### Directrice : Nancy Ward

Votre directrice est Nancy Ward. La directrice de l’Unité des services et communications veille à l’application des politiques et supervise la création, l’exécution et l’évaluation des programmes de formation ainsi que les vérifications. Elle a également la responsabilité de superviser tous les canaux de communication internes et externes, y compris le contenu Web en ligne.

#### Gestionnaire : Claude Huard (vous)

Votre rôle en tant que gestionnaire de l’Équipe de l’assurance de la qualité est de superviser la révision de contenu et de formuler des recommandations finales au sujet des manuels de formation, des spécifications de formation et d’autres documents de formation connexes. Votre rôle consiste également à formuler des recommandations en matière de dotation, gérer le rendement des membres de l’équipe ainsi que coordonner l’échange d’information et d’expertise avec les partenaires et les intervenants. Le gestionnaire est également responsable d’assurer la conformité à la politique et aux normes professionnelles et de présenter aux cadres des rapports, lesquels comprennent des mises à jour, des échéanciers et les incidences budgétaires des projets.

#### Analystes de l’assurance de la qualité

Les membres de votre équipe sont Danny McBride, Serge Duplessis, Marina Richter, Mary Woodside, Charlie Wang et Jack Laurier. Tous les membres de l’équipe sont des analystes de l’assurance de la qualité et, par conséquent, des experts en documentation qui formulent des recommandations sur les documents de formation et le contenu en ligne.
""",
                language=l_french,
            ),
            item_text(
                item_id=i_team_information_2,
                text_detail="""### QA Team Responsibilities

The Quality Assurance Team is responsible for:

1. **Providing information management services.** Responsibilities include ensuring that organizational development training programs across the public service are well documented. This priority includes synthesizing a large volume of information from various government organizations, ensuring adherence to information security policies, and providing appropriate accessibility to archived documents.
2. **Reviewing online content.** Responsibilities include reviewing a large volume of information regarding organizational training programs from various clients and partners, ensuring adherence to internal and external communications policies, and making recommendations to executives for final approval before information dissemination.
3. **Reviewing training documentation.** Responsibilities include ensuring the completeness and quality of content in all organizational development training- related documents. This priority includes reviewing training instructions, scoring manuals, training specifications, statistical reports, and other training-related materials.

#### New initiatives

You have been mandated to make a recommendation on the adoption of an “off-the- shelf” online request processing system. The proposed system, called Serv, provides features that would facilitate the management of client and partner requests for content review and documentation services. This includes enhanced categorization and tracking of pending requests, customizable forms applications, and various report generators. The Information Technology (IT) Team of the ODC recently facilitated a pilot test with Serv that included Danny McBride, who is a member of the Quality Assurance Team. Danny came back with positive feedback on his experience with the Serv system. Your team has been discussing the proposal to introduce this new technology in hopes of improving your services.
""",
                language=l_english,
            ),
            item_text(
                item_id=i_team_information_2,
                text_detail="""### Responsabilités de l’Équipe de l’AQ

L’Équipe de l’assurance de la qualité doit s’acquitter de ce qui suit :

1. **Fournir des services de gestion de l’information.** L’équipe doit veiller à ce que les programmes en développement organisationnel au sein de la fonction publique soient bien documentés. Cette priorité comprend : synthétiser un grand volume de renseignements provenant de divers organismes gouvernementaux, s’assurer que les politiques sur la sécurité de l’information sont respectées et donner un accès approprié aux documents archivés.
2. **Examiner le contenu en ligne.** Les responsabilités de l’équipe comprennent les suivantes : Examiner un grand volume d’information sur les programmes de formation organisationnels de divers clients et partenaires, s’assurer que les politiques sur les communications internes et les communications externes sont respectées et formuler des recommandations aux cadres supérieurs aux fins d’approbation définitive avant la diffusion de l’information.
3. **Examiner les documents de formation.** L’équipe doit s’assurer de l’intégralité et de la qualité du contenu de tous les documents liés à la formation en développement organisationnel. Cette priorité inclut l’examen des instructions de formation, des guides de correction, des spécifications de la formation, des rapports statistiques et d’autres documents de formation connexes.

#### Nouvelles initiatives

Vous avez reçu le mandat de formuler une recommandation au sujet de l’adoption d’un système commercial de traitement des demandes en ligne. Le système proposé, appelé Serv, offre des fonctionnalités qui faciliteraient la gestion des demandes des clients et des partenaires qui cherchent à obtenir des services de révision du contenu et de gestion de la documentation. Cela inclut l’amélioration du processus de catégorisation et de suivi des demandes en attente, la personnalisation des formulaires de demande et divers générateurs de rapports. L’Équipe de la technologie de l’information (TI) du CDO a récemment fait un essai pilote de Serv auquel a participé Danny McBride, un des membres de l’Équipe de l’assurance de la qualité. Danny a donné des commentaires positifs sur son expérience avec le système Serv. Votre équipe discute actuellement de la proposition visant à introduire cette nouvelle technologie afin d’améliorer vos services.
""",
                language=l_french,
            ),
        ]
    )


def destroy_background_markdown(apps, schema_editor):
    # get models
    language = apps.get_model("custom_models", "Language")
    item_type = apps.get_model("custom_models", "ItemType")
    item = apps.get_model("custom_models", "Item")
    item_text = apps.get_model("custom_models", "ItemText")
    test = apps.get_model("custom_models", "Test")
    # get db alias
    db_alias = schema_editor.connection.alias
    # get language objects
    l_english = (
        language.objects.using(db_alias)
        .filter(ISO_Code_1="en", ISO_Code_2="en-ca")
        .last()
    )
    l_french = (
        language.objects.using(db_alias)
        .filter(ISO_Code_1="fr", ISO_Code_2="fr-ca")
        .last()
    )
    # get item_type objects
    it_background = (
        item_type.objects.using(db_alias).filter(type_desc="background").last()
    )
    it_markdown = item_type.objects.using(db_alias).filter(type_desc="markdown").last()

    # get item objects
    emib_sample_item_id = (
        test.objects.using(db_alias).filter(test_name="emibSampleTest").last().item_id
    )
    i_background = (
        item.objects.using(db_alias)
        .filter(parent_id=emib_sample_item_id, item_type_id=it_background, order=0)
        .last()
    )
    i_background_info = (
        item.objects.using(db_alias)
        .filter(parent_id=i_background, item_type_id=it_markdown, order=1)
        .last()
    )
    i_organizational_info = (
        item.objects.using(db_alias)
        .filter(parent_id=i_background, item_type_id=it_markdown, order=2)
        .last()
    )
    i_organizational_structure = (
        item.objects.using(db_alias)
        .filter(parent_id=i_background, item_type_id=it_markdown, order=3)
        .last()
    )
    i_team_information_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_background, item_type_id=it_markdown, order=4)
        .last()
    )
    i_team_information_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_background, item_type_id=it_markdown, order=5)
        .last()
    )

    # destroy item_text
    item_text.objects.using(db_alias).filter(
        item_id=i_background, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_background, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_background_info, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_background_info, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_organizational_info, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_organizational_info, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_organizational_structure, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_organizational_structure, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_team_information_1, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_team_information_1, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_team_information_2, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_team_information_2, language=l_french
    ).delete()

    # destroy items; inverted order as children must be deleted first
    i_background_info.delete()
    i_organizational_info.delete()
    i_organizational_structure.delete()
    i_team_information_1.delete()
    i_team_information_2.delete()
    i_background.delete()
    it_background.delete()
    it_markdown.delete()


class Migration(migrations.Migration):

    dependencies = [("custom_models", "0010_upload_stubbed_pizza_test")]

    operations = [
        migrations.RunPython(upload_background_markdown, destroy_background_markdown)
    ]

