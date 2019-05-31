# Generated by Django 2.1.7 on 2019-05-30 14:07
# Edited by J. Michael Cherry to populate the emib sample

from django.db import migrations


def upload_emib_sample(apps, schema_editor):
    # get models
    language = apps.get_model("custom_models", "Language")
    item_type = apps.get_model("custom_models", "ItemType")
    question_type = apps.get_model("custom_models", "QuestionType")
    item = apps.get_model("custom_models", "Item")
    item_text = apps.get_model("custom_models", "ItemText")
    question = apps.get_model("custom_models", "Question")
    # get db alias
    db_alias = schema_editor.connection.alias
    # create languages; do not use bulk_create since we need these objects later on
    l_english = language(ISO_Code_1="en", ISO_Code_2="en-ca")
    l_english.save()
    l_french = language(ISO_Code_1="fr", ISO_Code_2="fr-ca")
    l_french.save()

    # create item_types; do not use bulk_create since we need these objects later on
    it_test = item_type(type_desc="test")
    it_test.save()
    it_question = item_type(type_desc="question")
    it_question.save()
    it_subject = item_type(type_desc="subject")
    it_subject.save()
    it_from = item_type(type_desc="from")
    it_from.save()
    it_to = item_type(type_desc="to")
    it_to.save()
    it_date = item_type(type_desc="date")
    it_date.save()
    it_body = item_type(type_desc="body")
    it_body.save()

    # create quesion_types; do not use bulk_create since we need these objects later on
    qt_email = question_type(question_type_desc="email")
    qt_email.save()

    # create items; do not use bulk_create since we need these objects later on
    # test
    i_emib = item(item_type_id=it_test, order=1)
    i_emib.save()

    # question 1 items
    i_q1 = item(parent_id=i_emib,
                item_type_id=it_question, order=1)
    i_q1.save()

    i_q1_subject = item(parent_id=i_q1,
                        item_type_id=it_subject, order=1)
    i_q1_subject.save()

    i_q1_from = item(parent_id=i_q1,
                     item_type_id=it_from, order=2)
    i_q1_from.save()

    i_q1_to = item(parent_id=i_q1,
                   item_type_id=it_to, order=3)
    i_q1_to.save()

    i_q1_date = item(parent_id=i_q1,
                     item_type_id=it_date, order=4)
    i_q1_date.save()

    i_q1_body = item(parent_id=i_q1,
                     item_type_id=it_body, order=5)
    i_q1_body.save()

    # question 2 items
    i_q2 = item(parent_id=i_emib,
                item_type_id=it_question, order=2)
    i_q2.save()

    i_q2_subject = item(parent_id=i_q2,
                        item_type_id=it_subject, order=1)
    i_q2_subject.save()

    i_q2_from = item(parent_id=i_q2,
                     item_type_id=it_from, order=2)
    i_q2_from.save()

    i_q2_to = item(parent_id=i_q2,
                   item_type_id=it_to, order=3)
    i_q2_to.save()

    i_q2_date = item(parent_id=i_q2,
                     item_type_id=it_date, order=4)
    i_q2_date.save()

    i_q2_body = item(parent_id=i_q2,
                     item_type_id=it_body, order=5)
    i_q2_body.save()

    # question 3 items
    i_q3 = item(parent_id=i_emib,
                item_type_id=it_question, order=3)
    i_q3.save()

    i_q3_subject = item(parent_id=i_q3,
                        item_type_id=it_subject, order=1)
    i_q3_subject.save()

    i_q3_from = item(parent_id=i_q3,
                     item_type_id=it_from, order=2)
    i_q3_from.save()

    i_q3_to = item(parent_id=i_q3,
                   item_type_id=it_to, order=3)
    i_q3_to.save()

    i_q3_date = item(parent_id=i_q3,
                     item_type_id=it_date, order=4)
    i_q3_date.save()

    i_q3_body = item(parent_id=i_q3,
                     item_type_id=it_body, order=5)
    i_q3_body.save()

    # bulk create questions
    question.objects.using(db_alias).bulk_create([
        question(question_type_id=qt_email, item_id=i_q1),
        question(question_type_id=qt_email, item_id=i_q2),
        question(question_type_id=qt_email, item_id=i_q3)
    ])

    # bulk create item_text
    item_text.objects.using(db_alias).bulk_create([
        item_text(item_id=i_emib, text_detail="eMiB Sample Test",
                  language=l_english),
        item_text(item_id=i_emib, text_detail="FR eMiB Sample Test",
                  language=l_french),
        item_text(item_id=i_q1, text_detail="Question 1", language=l_english),
        item_text(item_id=i_q1, text_detail="FR Question 1",
                  language=l_french),
        item_text(item_id=i_q1_subject,
                  text_detail="Bad experience with Serv", language=l_english),
        item_text(item_id=i_q1_subject,
                  text_detail="Mauvaise expérience avec Serv", language=l_french),
        item_text(item_id=i_q1_from,
                  text_detail="Serge Duplessis (Quality Control Analyst, Quality Assurance Team)", language=l_english),
        item_text(item_id=i_q1_from, text_detail="Serge Duplessis (analyste de l’assurance de la qualité, Équipe de l’assurance de la qualité)", language=l_french),
        item_text(item_id=i_q1_to,
                  text_detail="Claude Huard (Manager, Quality Assurance Team)", language=l_english),
        item_text(item_id=i_q1_to,
                  text_detail="Claude Huard (gestionnaire, Équipe de l’assurance de la qualité)", language=l_french),
        item_text(item_id=i_q1_date,
                  text_detail="Thursday, November 3", language=l_english),
        item_text(item_id=i_q1_date,
                  text_detail="Le jeudi 3 novembre", language=l_french),
        item_text(item_id=i_q1_body, text_detail="Hello Claude,\n\nAs you are settling into this position, I was hoping to share with you some of my thoughts about the proposed changes to our service requests and documentation practices.\n\nI have been working on the Quality Assurance team for over 12 years. I feel that, overall, we are quite successful in understanding and processing service requests. Switching to an automated, computerized system would take a very long time to adapt to and could jeopardize the quality of our service. For example, having a face-to-face or telephone conversation with a client can help us better understand the client’s issues in more depth because it allows us to ask probing questions and receive important information related to each case. By buying into this new technology, we risk having more IT problems and unexpected delays in the long-run.\n\nI have voiced my opinion in previous meetings but I do not feel that my opinions matter. Everyone else has been on the team for less than two years and I feel ignored because I’m the oldest member on the team. I urge you to consider my opinion so that we do not make a costly mistake.\n\nSerge", language=l_english),
        item_text(item_id=i_q1_body, text_detail="Bonjour Claude.Alors que vous vous familiarisez avec vos nouvelles fonctions, j’aimerais vous faire part de certaines de mes opinions concernant les changements que l’on propose d’apporter à notre système de demandes de services et à nos pratiques en matière de documentation.\n\nJe travaille au sein de l’Équipe de l’assurance de la qualité depuis plus de 12 ans. J’estime que, dans l’ensemble, nous avons bien réussi à comprendre et à traiter les demandes de service. Le passage à un système automatisé et informatisé prendrait beaucoup de temps avant qu’on s’y adapte et pourrait compromettre la qualité de notre service. Par exemple, une conversation en personne ou par téléphone avec un client peut nous aider à mieux comprendre ses problèmes, car cela nous permet de poser des questions d’approfondissement et d’obtenir des renseignements importants sur chaque cas. En adoptant cette nouvelle technologie, nous risquons d’avoir plus de problèmes de TI et des retards imprévus à long terme.\n\nJ’ai déjà exprimé mon opinion lors de réunions précédentes, mais je n’ai pas l’impression que mes opinions comptent. Tous les autres sont dans l’équipe depuis moins de deux ans et je me sens ignoré parce que je suis le plus âgé de l’équipe. Je vous encourage à tenir compte de mon opinion afin que nous ne commettions pas une erreur coûteuse. \n\nSerge", language=l_french),
        item_text(item_id=i_q2, text_detail="Question 2", language=l_english),
        item_text(item_id=i_q2, text_detail="FR Question 2",
                  language=l_french),
        item_text(item_id=i_q2_subject,
                  text_detail="Informal Training on Serv", language=l_english),
        item_text(item_id=i_q2_subject,
                  text_detail="Formation informelle sur Serv", language=l_french),
        item_text(item_id=i_q2_from,
                  text_detail="Marina Richter (Quality Control Analyst, Quality Assurance Team)", language=l_english),
        item_text(item_id=i_q2_from, text_detail="Marina Richter (analyste de l’assurance de la qualité, Équipe de l’assurance de la qualité)", language=l_french),
        item_text(item_id=i_q2_to,
                  text_detail="Claude Huard (Manager, Quality Assurance Team)", language=l_english),
        item_text(item_id=i_q2_to,
                  text_detail="Claude Huard (gestionnaire, Équipe de l’assurance de la qualité)", language=l_french),
        item_text(item_id=i_q2_date,
                  text_detail="Friday, November 4", language=l_english),
        item_text(item_id=i_q2_date,
                  text_detail="Le vendredi 4 novembre", language=l_french),
        item_text(item_id=i_q2_body, text_detail="Hello Claude,\n\nDuring our last meeting, Danny had mentioned that he learned a lot about the Serv system during the pilot testing exercise with the IT unit.  While talking to other team members, some mentioned they were trained on and worked with an older version of Serv in previous jobs. However, there are a few of us who have never used it. I would like to know if there would be opportunities to be trained on Serv?\n\nMarina", language=l_english),
        item_text(item_id=i_q2_body, text_detail="Bonjour Claude.\nLors de notre dernière réunion, Danny a indiqué qu’il avait beaucoup appris sur le système Serv  pendant l’exercice d’essai pilote avec l’Équipe des TI. En discutant avec d’autres membres de notre équipe, certains ont mentionné qu’ils avaient reçu une formation et avaient travaillé avec une ancienne version de Serv dans des emplois antérieurs. Cependant, certains d’entre nous ne l’ont jamais utilisée. J’aimerais savoir s’il y aurait des possibilités d’être formé sur Serv ?\nMarina", language=l_french),
        item_text(item_id=i_q3, text_detail="Question 3", language=l_english),
        item_text(item_id=i_q3, text_detail="FR Question 3",
                  language=l_french),
        item_text(item_id=i_q3_subject,
                  text_detail="Report deadline", language=l_english),
        item_text(item_id=i_q3_subject,
                  text_detail="Date limite de dépôt du rapport", language=l_french),
        item_text(item_id=i_q3_from,
                  text_detail="Charlie Wang (Quality Control Analyst, Quality Assurance Team)", language=l_english),
        item_text(item_id=i_q3_from, text_detail="Charlie Wang (analyste de l’assurance de la qualité, Équipe de l’assurance de la qualité)", language=l_french),
        item_text(item_id=i_q3_to,
                  text_detail="Claude Huard (Manager, Quality Assurance Team)", language=l_english),
        item_text(item_id=i_q3_to,
                  text_detail="Claude Huard (gestionnaire, Équipe de l’assurance de la qualité)", language=l_french),
        item_text(item_id=i_q3_date,
                  text_detail="Friday, November 4", language=l_english),
        item_text(item_id=i_q3_date,
                  text_detail="Le vendredi 4 novembre", language=l_french),
        item_text(item_id=i_q3_body, text_detail="Hello Claude,\n\nI am working with Clara Farewell from the Research and Innovations unit on evaluating the quality of a training approach and I am having a hard time getting a hold of her. I am starting to be concerned because I have been waiting on her part of the work to complete the evaluation report.\nFor the past three weeks, we had scheduled working meetings on Friday afternoons and although she did cancel the first one, she was absent the past two, without notice. She did not answer my attempts to contact her by phone or email. I am worried that I will not be able to complete the report by the end of next Friday without her content.\n\nOn another note, I was told by one of my colleagues from the Program Development unit that his director, Bartosz Greco, would invite employees from other units to help them develop a new training program. They want to take a multiple perspectives approach. I’m very much interested in participating in this process. As usual, manager permission is required for participation. I am wondering what you think?\n\nThank you,\nCharlie", language=l_english),
        item_text(item_id=i_q3_body, text_detail="Bonjour Claude.\nJe travaille avec Clara Farewell de l’Unité de recherche et innovations sur l’évaluation de la qualité d’une approche de formation et j’ai de la difficulté à la joindre. Je commence à m’inquiéter parce que j’attendais qu’elle termine sa partie du travail pour achever le rapport d’évaluation.\nAu cours des trois dernières semaines, nous avions prévu des rencontres de travail les vendredis après-midi et, après avoir annulé la première rencontre, elle était absente aux deux dernières, sans donner un préavis. Elle n’a pas non plus répondu à mes tentatives de communiquer avec elle par téléphone ou par courriel. Je m’inquiète de ne pas pouvoir terminer le rapport d’ici vendredi prochain sans sa part du travail.\nDans un autre ordre d’idées, un de mes collègues de l’Unité de développement des programmes m’a dit que son directeur, Bartosz Greco, inviterait des employés d’autres unités à les aider à créer un nouveau programme de formation. Ils veulent adopter une approche qui inclut des perspectives multiples. J’aimerais bien participer à ce processus. Comme d’habitude, la permission du gestionnaire est requise pour y participer. Je me demande ce que tu en penses.\nMerci,\nCharlie", language=l_french)
    ])


def destroy_emib_sample(apps, schema_editor):
    # get models
    language = apps.get_model("custom_models", "Language")
    item_type = apps.get_model("custom_models", "ItemType")
    question_type = apps.get_model("custom_models", "QuestionType")
    item = apps.get_model("custom_models", "Item")
    item_text = apps.get_model("custom_models", "ItemText")
    question = apps.get_model("custom_models", "Question")
    # get db alias
    db_alias = schema_editor.connection.alias
    # get language objects
    l_english = language.objects.using(db_alias).filter(
        ISO_Code_1="en", ISO_Code_2="en-ca").last()
    l_french = language.objects.using(db_alias).filter(
        ISO_Code_1="fr", ISO_Code_2="fr-ca").last()
    # get item_type objects
    it_test = item_type.objects.using(db_alias).filter(type_desc="test").last()
    it_question = item_type.objects.using(
        db_alias).filter(type_desc="question").last()
    it_subject = item_type.objects.using(
        db_alias).filter(type_desc="subject").last()
    it_from = item_type.objects.using(db_alias).filter(type_desc="from").last()
    it_to = item_type.objects.using(db_alias).filter(type_desc="to").last()
    it_date = item_type.objects.using(db_alias).filter(type_desc="date").last()
    it_body = item_type.objects.using(db_alias).filter(type_desc="body").last()
    # get question_type objects
    qt_email = question_type.objects.using(
        db_alias).filter(question_type_desc="email").last()
    # get item objects
    i_emib = item.objects.using(db_alias).filter(
        item_type_id=it_test, order=1).last()
    i_q1 = item.objects.using(db_alias).filter(
        parent_id=i_emib, item_type_id=it_question, order=1).last()
    i_q1_subject = item.objects.using(db_alias).filter(
        parent_id=i_q1, item_type_id=it_subject, order=1).last()
    i_q1_from = item.objects.using(db_alias).filter(
        parent_id=i_q1, item_type_id=it_from, order=2).last()
    i_q1_to = item.objects.using(db_alias).filter(
        parent_id=i_q1, item_type_id=it_to, order=3).last()
    i_q1_date = item.objects.using(db_alias).filter(
        parent_id=i_q1, item_type_id=it_date, order=4).last()
    i_q1_body = item.objects.using(db_alias).filter(
        parent_id=i_q1, item_type_id=it_body, order=5).last()
    i_q2 = item.objects.using(db_alias).filter(
        parent_id=i_emib, item_type_id=it_question, order=2).last()
    i_q2_subject = item.objects.using(db_alias).filter(
        parent_id=i_q2, item_type_id=it_subject, order=1).last()
    i_q2_from = item.objects.using(db_alias).filter(
        parent_id=i_q2, item_type_id=it_from, order=2).last()
    i_q2_to = item.objects.using(db_alias).filter(
        parent_id=i_q2, item_type_id=it_to, order=3).last()
    i_q2_date = item.objects.using(db_alias).filter(
        parent_id=i_q2, item_type_id=it_date, order=4).last()
    i_q2_body = item.objects.using(db_alias).filter(
        parent_id=i_q2, item_type_id=it_body, order=5).last()
    i_q3 = item.objects.using(db_alias).filter(
        parent_id=i_emib, item_type_id=it_question, order=3).last()
    i_q3_subject = item.objects.using(db_alias).filter(
        parent_id=i_q3, item_type_id=it_subject, order=1).last()
    i_q3_from = item.objects.using(db_alias).filter(
        parent_id=i_q3, item_type_id=it_from, order=2).last()
    i_q3_to = item.objects.using(db_alias).filter(
        parent_id=i_q3,   item_type_id=it_to, order=3).last()
    i_q3_date = item.objects.using(db_alias).filter(
        parent_id=i_q3, item_type_id=it_date, order=4).last()
    i_q3_body = item.objects.using(db_alias).filter(
        parent_id=i_q3, item_type_id=it_body, order=5).last()

    # destroy questions
    question.objects.using(db_alias).filter(
        question_type_id=qt_email, item_id=i_q1).delete()
    question.objects.using(db_alias).filter(
        question_type_id=qt_email, item_id=i_q2).delete()
    question.objects.using(db_alias).filter(
        question_type_id=qt_email, item_id=i_q3).delete()

        # destroy item_text
    item_text.objects.using(db_alias).filter(item_id=i_emib, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_emib, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1,language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_subject,language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_subject, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_from, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_from, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_to, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_to, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_date, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_date, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_body, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q1_body, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_subject, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_subject, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_from, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_from, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_to, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_to, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_date, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_date, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_body, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q2_body, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_subject, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_subject, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_from, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_from, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_to, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_to, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_date, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_date, language=l_french).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_body, language=l_english).delete()
    item_text.objects.using(db_alias).filter(item_id=i_q3_body, language=l_french).delete()

    # destroy items; inverted order as children must be deleted first
    i_q3_body.delete()
    i_q3_date.delete()
    i_q3_to.delete()
    i_q3_from.delete()
    i_q3_subject.delete()
    i_q3.delete()
    i_q2_body.delete()
    i_q2_date.delete()
    i_q2_to.delete()
    i_q2_from.delete()
    i_q2_subject.delete()
    i_q2.delete()
    i_q1_body.delete()
    i_q1_date.delete()
    i_q1_to.delete()
    i_q1_from.delete()
    i_q1_subject.delete()
    i_q1.delete()
    i_emib.delete()

    # destroy question_types
    qt_email.delete()

    # destroy item_types
    it_test.delete()
    it_question.delete()
    it_subject.delete()
    it_from.delete()
    it_to.delete()
    it_date.delete()
    it_body.delete()

    # destroy languages
    l_english.delete()
    l_french.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('custom_models', '0004_auto_20190529_0846'),
    ]

    operations = [
        migrations.RunPython(upload_emib_sample, destroy_emib_sample),
    ]
