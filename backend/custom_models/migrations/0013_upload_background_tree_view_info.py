# Generated by Django 2.1.7 on 2019-05-30 14:07
# Edited by Francis Normand to upload the background tree view
# content (one in Organizational Structure section and one in Team
# Information section) of the image descriptions for the sample test

from django.db import migrations


def upload_background_tree_view_info(apps, schema_editor):
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
    it_background = (
        item_type.objects.using(db_alias).filter(type_desc="background").last()
    )
    background_id = (
        item.objects.using(db_alias)
        .filter(parent_id=emib_sample_item_id, item_type_id=it_background, order=0)
        .last()
    )

    # create item_types; do not use bulk_create since we need these objects later on
    it_tree_view = item_type(type_desc="tree-view")
    it_tree_view.save()
    it_organizational_structure_tree_child = item_type(type_desc="organizational-structure-tree-child")
    it_organizational_structure_tree_child.save()
    it_team_information_tree_child = item_type(type_desc="team-information-tree-child")
    it_team_information_tree_child.save()

    # create items; do not use bulk_create since we need these objects later on
    # organizational structure tree view
    i_tree_view_of_org_structure = item(
        parent_id=background_id, item_type_id=it_tree_view, order=1
    )
    i_tree_view_of_org_structure.save()

    # organizational structure tree view children
    i_tree_view_of_org_structure_person_1 = item(
        parent_id=i_tree_view_of_org_structure, item_type_id=it_organizational_structure_tree_child, order=1
    )
    i_tree_view_of_org_structure_person_1.save()
    i_tree_view_of_org_structure_person_2 = item(
        parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=1
    )
    i_tree_view_of_org_structure_person_2.save()
    i_tree_view_of_org_structure_person_3 = item(
        parent_id=i_tree_view_of_org_structure_person_2, item_type_id=it_organizational_structure_tree_child, order=1
    )
    i_tree_view_of_org_structure_person_3.save()
    i_tree_view_of_org_structure_person_4 = item(
        parent_id=i_tree_view_of_org_structure_person_2, item_type_id=it_organizational_structure_tree_child, order=2
    )
    i_tree_view_of_org_structure_person_4.save()
    i_tree_view_of_org_structure_person_5 = item(
        parent_id=i_tree_view_of_org_structure_person_2, item_type_id=it_organizational_structure_tree_child, order=3
    )
    i_tree_view_of_org_structure_person_5.save()
    i_tree_view_of_org_structure_person_6 = item(
        parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=2
    )
    i_tree_view_of_org_structure_person_6.save()
    i_tree_view_of_org_structure_person_7 = item(
        parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=3
    )
    i_tree_view_of_org_structure_person_7.save()
    i_tree_view_of_org_structure_person_8 = item(
        parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=4
    )
    i_tree_view_of_org_structure_person_8.save()
    i_tree_view_of_org_structure_person_9 = item(
        parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=1
    )
    i_tree_view_of_org_structure_person_9.save()
    i_tree_view_of_org_structure_person_10 = item(
        parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=2
    )
    i_tree_view_of_org_structure_person_10.save()
    i_tree_view_of_org_structure_person_11 = item(
        parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=3
    )
    i_tree_view_of_org_structure_person_11.save()
    i_tree_view_of_org_structure_person_12 = item(
        parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=4
    )
    i_tree_view_of_org_structure_person_12.save()

    # team information tree view
    i_tree_view_of_team_info = item(
        parent_id=background_id, item_type_id=it_tree_view, order=2
    )
    i_tree_view_of_team_info.save()

    # team information tree view children
    i_tree_view_of_team_info_person_1 = item(
        parent_id=i_tree_view_of_team_info, item_type_id=it_team_information_tree_child, order=1
    )
    i_tree_view_of_team_info_person_1.save()
    i_tree_view_of_team_info_person_2 = item(
        parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=1
    )
    i_tree_view_of_team_info_person_2.save()
    i_tree_view_of_team_info_person_3 = item(
        parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=2
    )
    i_tree_view_of_team_info_person_3.save()
    i_tree_view_of_team_info_person_4 = item(
        parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=3
    )
    i_tree_view_of_team_info_person_4.save()
    i_tree_view_of_team_info_person_5 = item(
        parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=4
    )
    i_tree_view_of_team_info_person_5.save()
    i_tree_view_of_team_info_person_6 = item(
        parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=5
    )
    i_tree_view_of_team_info_person_6.save()
    i_tree_view_of_team_info_person_7 = item(
        parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=6
    )
    i_tree_view_of_team_info_person_7.save()

    # bulk create item_text
    item_text.objects.using(db_alias).bulk_create(
        [
            item_text(
                item_id=i_tree_view_of_org_structure_person_1,
                text_detail="Jenna Icard (President)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_1,
                text_detail="Jenna Icard (Présidente)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_2,
                text_detail="Amari Kinsler (Corporate Affairs Director)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_2,
                text_detail="Amari Kinsler (Directeur, Affaires ministérielles)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_3,
                text_detail="Marc Sheridan (Human Resources Manager)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_3,
                text_detail="Marc Sheridan (Gestionnaire, Ressources humaines)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_4,
                text_detail="Bob McNutt (Finance Manager)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_4,
                text_detail="Bob McNutt (Gestionnaire, Finances)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_5,
                text_detail="Lana Hussad (Information Technology Manager)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_5,
                text_detail="Lana Hussad (Gestionnaire, Technologies de l'information)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_6,
                text_detail="Geneviève Bédard (Research and Innovations Director)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_6,
                text_detail="Geneviève Bédard (Directrice, Recherche et innovations)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_7,
                text_detail="Bartosz Greco (Program Development Director)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_7,
                text_detail="Bartosz Greco (Directeur, Développement de programmes)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_8,
                text_detail="Nancy Ward (Services and Communications Director)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_8,
                text_detail="Nancy Ward (Directrice, Services et communications)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_9,
                text_detail="Claude Huard (Quality Assurance Manager - You)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_9,
                text_detail="Claude Huard (Gestionnaire, Assurance de la qualité - vous)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_10,
                text_detail="Haydar Kalil (Services and Support Manager)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_10,
                text_detail="Haydar Kalil (Gestionnaire, Service et soutien)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_11,
                text_detail="Geoffrey Hamma (Audits Manager)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_11,
                text_detail="Geoffrey Hamma (Gestionnaire, Vérifications)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_12,
                text_detail="Lucy Trang (E-Training Manager)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_org_structure_person_12,
                text_detail="Lucy Trang (Gestionnaire, Formation en ligne)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_1,
                text_detail="Claude Huard (Quality Assurance Manager - You)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_1,
                text_detail="Claude Huard (Gestionnaire, Assurance de la qualité - vous)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_2,
                text_detail="Danny McBride (QA Analyst)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_2,
                text_detail="Danny McBride (Analyste de l’assurance de la qualité)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_3,
                text_detail="Serge Duplessis (QA Analyst)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_3,
                text_detail="Serge Duplessis (Analyste de l’assurance de la qualité)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_4,
                text_detail="Marina Richter (QA Analyst)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_4,
                text_detail="Marina Richter (Analyste de l’assurance de la qualité)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_5,
                text_detail="Mary Woodside (QA Analyst)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_5,
                text_detail="Mary Woodside (Analyste de l’assurance de la qualité)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_6,
                text_detail="Charlie Wang (QA Analyst)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_6,
                text_detail="Charlie Wang (Analyste de l’assurance de la qualité)",
                language=l_french,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_7,
                text_detail="Jack Laurier (QA Analyst)",
                language=l_english,
            ),
            item_text(
                item_id=i_tree_view_of_team_info_person_7,
                text_detail="Jack Laurier (Analyste de l’assurance de la qualité)",
                language=l_french,
            ),
        ]
    )


def destroy_background_tree_view_info(apps, schema_editor):
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
    it_tree_view = (
        item_type.objects.using(db_alias).filter(type_desc="tree-view").last()
    )
    it_organizational_structure_tree_child = (
        item_type.objects.using(db_alias).filter(type_desc="organizational-structure-tree-child").last()
    )
    it_team_information_tree_child = (
        item_type.objects.using(db_alias).filter(type_desc="team-information-tree-child").last()
    )

    # get item objects
    emib_sample_item_id = (
        test.objects.using(db_alias).filter(test_name="emibSampleTest").last().item_id
    )
    it_background = (
        item_type.objects.using(db_alias).filter(type_desc="background").last()
    )
    background_id = (
        item.objects.using(db_alias)
        .filter(parent_id=emib_sample_item_id, item_type_id=it_background, order=0)
        .last()
    )
    i_tree_view_of_org_structure = (
        item.objects.using(db_alias)
        .filter(parent_id=background_id, item_type_id=it_tree_view, order=1)
        .last()
    )
    i_tree_view_of_org_structure_person_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure, item_type_id=it_organizational_structure_tree_child, order=1)
        .last()
    )
    i_tree_view_of_org_structure_person_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=1)
        .last()
    )
    i_tree_view_of_org_structure_person_3 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_2, item_type_id=it_organizational_structure_tree_child, order=1)
        .last()
    )
    i_tree_view_of_org_structure_person_4 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_2, item_type_id=it_organizational_structure_tree_child, order=2)
        .last()
    )
    i_tree_view_of_org_structure_person_5 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_2, item_type_id=it_organizational_structure_tree_child, order=3)
        .last()
    )
    i_tree_view_of_org_structure_person_6 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=2)
        .last()
    )
    i_tree_view_of_org_structure_person_7 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=3)
        .last()
    )
    i_tree_view_of_org_structure_person_8 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_1, item_type_id=it_organizational_structure_tree_child, order=4)
        .last()
    )
    i_tree_view_of_org_structure_person_9 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=1)
        .last()
    )
    i_tree_view_of_org_structure_person_10 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=2)
        .last()
    )
    i_tree_view_of_org_structure_person_11 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=3)
        .last()
    )
    i_tree_view_of_org_structure_person_12 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_org_structure_person_8, item_type_id=it_organizational_structure_tree_child, order=4)
        .last()
    )

    i_tree_view_of_team_info = (
        item.objects.using(db_alias)
        .filter(parent_id=background_id, item_type_id=it_tree_view, order=2)
        .last()
    )
    i_tree_view_of_team_info_person_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_team_info, item_type_id=it_team_information_tree_child, order=1)
        .last()
    )
    i_tree_view_of_team_info_person_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=1)
        .last()
    )
    i_tree_view_of_team_info_person_3 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=2)
        .last()
    )
    i_tree_view_of_team_info_person_4 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=3)
        .last()
    )
    i_tree_view_of_team_info_person_5 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=4)
        .last()
    )
    i_tree_view_of_team_info_person_6 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=5)
        .last()
    )
    i_tree_view_of_team_info_person_7 = (
        item.objects.using(db_alias)
        .filter(parent_id=i_tree_view_of_team_info_person_1, item_type_id=it_team_information_tree_child, order=6)
        .last()
    )

    # destroy item_text
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_1, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_1, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_2, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_2, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_3, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_3, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_4, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_4, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_5, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_5, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_6, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_6, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_7, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_7, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_8, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_8, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_9, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_9, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_10, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_10, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_11, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_11, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_12, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure_person_12, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_org_structure, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_1, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_1, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_2, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_2, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_3, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_3, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_4, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_4, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_5, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_5, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_6, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_6, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_7, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info_person_7, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=i_tree_view_of_team_info, language=l_french
    ).delete()

    # destroy items; inverted order as children must be deleted first
    i_tree_view_of_org_structure_person_1.delete()
    i_tree_view_of_org_structure_person_2.delete()
    i_tree_view_of_org_structure_person_3.delete()
    i_tree_view_of_org_structure_person_4.delete()
    i_tree_view_of_org_structure_person_5.delete()
    i_tree_view_of_org_structure_person_6.delete()
    i_tree_view_of_org_structure_person_7.delete()
    i_tree_view_of_org_structure_person_8.delete()
    i_tree_view_of_org_structure_person_9.delete()
    i_tree_view_of_org_structure_person_10.delete()
    i_tree_view_of_org_structure_person_11.delete()
    i_tree_view_of_org_structure_person_12.delete()
    i_tree_view_of_org_structure.delete()
    i_tree_view_of_team_info_person_1.delete()
    i_tree_view_of_team_info_person_2.delete()
    i_tree_view_of_team_info_person_3.delete()
    i_tree_view_of_team_info_person_4.delete()
    i_tree_view_of_team_info_person_5.delete()
    i_tree_view_of_team_info_person_6.delete()
    i_tree_view_of_team_info_person_7.delete()
    i_tree_view_of_team_info.delete()
    it_team_information_tree_child.delete()
    it_organizational_structure_tree_child.delete()
    it_tree_view.delete()


class Migration(migrations.Migration):

    dependencies = [("custom_models", "0012_update_emib_sample_fr")]

    operations = [
        migrations.RunPython(
            upload_background_tree_view_info, destroy_background_tree_view_info
        )
    ]
