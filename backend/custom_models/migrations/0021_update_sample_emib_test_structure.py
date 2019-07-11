# Generated by Django 2.1.7 on 2019-06-03 15:27
# Edited by J. Michael Cherry to correct the pizza test time limit

from django.db import migrations
from datetime import datetime  


def reoder_emib_test(apps, schema_editor):
    # get models
    language = apps.get_model("custom_models", "Language")
    item_type = apps.get_model("custom_models", "ItemType")
    item = apps.get_model("custom_models", "Item")
    item_text = apps.get_model("custom_models", "ItemText")
    test = apps.get_model("custom_models", "Test")
    # get db alias
    db_alias = schema_editor.connection.alias

    # get language id and test
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

    # get item_types
    it_sections = item_type.objects.using(db_alias).filter(type_desc="sections").last()
    it_section = item_type.objects.using(db_alias).filter(type_desc="section").last()
    it_background = (
        item_type.objects.using(db_alias).filter(type_desc="background").last()
    )
    it_markdown = item_type.objects.using(db_alias).filter(type_desc="markdown").last()
    it_tree_view = (
        item_type.objects.using(db_alias).filter(type_desc="tree_view").last()
    )

    # get the background item
    background = (
        item.objects.using(db_alias)
        .filter(parent_id=emib_sample_item_id, item_type_id=it_background, order=0)
        .last()
    )

    # get all markdown children
    markdown_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=1)
        .last()
    )
    markdown_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=2)
        .last()
    )
    markdown_3 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=3)
        .last()
    )
    markdown_4 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=4)
        .last()
    )
    markdown_5 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=5)
        .last()
    )
    markdown_6 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=6)
        .last()
    )
    markdown_7 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=7)
        .last()
    )
    markdown_8 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=8)
        .last()
    )
    markdown_9 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=9)
        .last()
    )

    # get all tree_view children
    tree_view_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_tree_view, order=1)
        .last()
    )
    tree_view_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_tree_view, order=2)
        .last()
    )

    # create sections
    sections = item(parent_id=emib_sample_item_id, item_type_id=it_sections, order=1)
    sections.save()

    section_1 = item(parent_id=sections, item_type_id=it_section, order=1)
    section_1.save()
    section_2 = item(parent_id=sections, item_type_id=it_section, order=2)
    section_2.save()
    section_3 = item(parent_id=sections, item_type_id=it_section, order=3)
    section_3.save()
    section_4 = item(parent_id=sections, item_type_id=it_section, order=4)
    section_4.save()

    # bulk create section and tree_view text
    item_text.objects.using(db_alias).bulk_create(
        [
            item_text(item_id=section_1, text_detail="Overview", language=l_english),
            item_text(item_id=section_1, text_detail="Contexte", language=l_french),
            item_text(
                item_id=section_2, text_detail="Your organization", language=l_english
            ),
            item_text(
                item_id=section_2, text_detail="FR Your organization", language=l_french
            ),
            item_text(
                item_id=section_3,
                text_detail="Organizational Structure",
                language=l_english,
            ),
            item_text(
                item_id=section_3,
                text_detail="Structure organisationnelle",
                language=l_french,
            ),
            item_text(item_id=section_4, text_detail="Your team", language=l_english),
            item_text(item_id=section_4, text_detail="FR Your team", language=l_french),
            item_text(
                item_id=tree_view_1,
                text_detail="The Organizational Chart of the ODC",
                language=l_english,
            ),
            item_text(
                item_id=tree_view_1, text_detail="Organigramme (CDO)", language=l_french
            ),
            item_text(
                item_id=tree_view_2,
                text_detail="The Organizational Chart of the QA Team",
                language=l_english,
            ),
            item_text(
                item_id=tree_view_2,
                text_detail="Organigramme Équipe de l'assurance de la qualité (AQ)",
                language=l_french,
            ),
        ]
    )

    # move markdowns and tree_view to belong to the correct parents
    markdown_1.parent_id = section_1
    markdown_1.order = 1
    markdown_1.save()

    markdown_2.parent_id = section_2
    markdown_2.order = 1
    markdown_2.save()

    markdown_3.parent_id = section_3
    markdown_3.order = 1
    markdown_3.save()
    tree_view_1.parent_id = section_3
    tree_view_1.order = 2
    tree_view_1.save()

    markdown_4.parent_id = section_4
    markdown_4.order = 1
    markdown_4.save()
    tree_view_2.parent_id = section_4
    tree_view_2.order = 2
    tree_view_2.save()
    markdown_5.parent_id = section_4
    markdown_5.order = 3
    markdown_5.save()

    # TODO reorder markdown and tree-view parentage
    # section_1-> markdown_1
    # section_2 -> markdown_2
    # section_3 -> [markdown_3, tree_view_1]
    # section_4 -> [markdown_4, tree_view_2, markdown_5]
    expiry_date = datetime.now()
    # TODO expire background
    # expire markdown_6, markdown_7, markdown_8, markdown_9
    markdown_6.date_to = expiry_date
    markdown_6.save()
    markdown_7.date_to = expiry_date
    markdown_7.save()
    markdown_8.date_to = expiry_date
    markdown_8.save()
    markdown_9.date_to = expiry_date
    markdown_9.save()


def rollback_emib_test(apps, schema_editor):
    # get models
    language = apps.get_model("custom_models", "Language")
    item_type = apps.get_model("custom_models", "ItemType")
    item = apps.get_model("custom_models", "Item")
    item_text = apps.get_model("custom_models", "ItemText")
    test = apps.get_model("custom_models", "Test")
    # get db alias
    db_alias = schema_editor.connection.alias

    # get language id and test
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

    # get item_types
    it_sections = item_type.objects.using(db_alias).filter(type_desc="sections").last()
    it_section = item_type.objects.using(db_alias).filter(type_desc="section").last()
    it_background = (
        item_type.objects.using(db_alias).filter(type_desc="background").last()
    )
    it_markdown = item_type.objects.using(db_alias).filter(type_desc="markdown").last()
    it_tree_view = (
        item_type.objects.using(db_alias).filter(type_desc="tree_view").last()
    )

    # get the background item
    background = (
        item.objects.using(db_alias)
        .filter(parent_id=emib_sample_item_id, item_type_id=it_background, order=0)
        .last()
    )

    # get sections
    sections = (
        item.objects.using(db_alias)
        .filter(parent_id=emib_sample_item_id, item_type_id=it_sections, order=1)
        .last()
    )

    section_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=sections, item_type_id=it_section, order=1)
        .last()
    )
    section_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=sections, item_type_id=it_section, order=2)
        .last()
    )
    section_3 = (
        item.objects.using(db_alias)
        .filter(parent_id=sections, item_type_id=it_section, order=3)
        .last()
    )
    section_4 = (
        item.objects.using(db_alias)
        .filter(parent_id=sections, item_type_id=it_section, order=4)
        .last()
    )

    # get the tree_views

    tree_view_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=section_3, item_type_id=it_tree_view, order=2)
        .last()
    )

    tree_view_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=section_4, item_type_id=it_tree_view, order=2)
        .last()
    )

    # Delete section and tree_view text
    item_text.objects.using(db_alias).filter(
        item_id=section_1, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=section_1, language=l_french
    ).delete()

    item_text.objects.using(db_alias).filter(
        item_id=section_2, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=section_2, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=section_3, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=section_3, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=section_4, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=section_4, language=l_french
    ).delete()

    item_text.objects.using(db_alias).filter(
        item_id=tree_view_1, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=tree_view_1, language=l_french
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=tree_view_2, language=l_english
    ).delete()
    item_text.objects.using(db_alias).filter(
        item_id=tree_view_2, language=l_french
    ).delete()

    # get markdowns
    markdown_1 = (
        item.objects.using(db_alias)
        .filter(parent_id=section_1, item_type_id=it_markdown, order=1)
        .last()
    )
    markdown_2 = (
        item.objects.using(db_alias)
        .filter(parent_id=section_2, item_type_id=it_markdown, order=1)
        .last()
    )
    markdown_3 = (
        item.objects.using(db_alias)
        .filter(parent_id=section_3, item_type_id=it_markdown, order=1)
        .last()
    )
    markdown_4 = (
        item.objects.using(db_alias)
        .filter(parent_id=section_4, item_type_id=it_markdown, order=1)
        .last()
    )
    markdown_5 = (
        item.objects.using(db_alias)
        .filter(parent_id=section_4, item_type_id=it_markdown, order=3)
        .last()
    )

    markdown_6 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=6)
        .last()
    )
    markdown_7 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=7)
        .last()
    )
    markdown_8 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=8)
        .last()
    )
    markdown_9 = (
        item.objects.using(db_alias)
        .filter(parent_id=background, item_type_id=it_markdown, order=9)
        .last()
    )

    # move markdowns and tree_view to belong to the correct parents
    # TODO markdown
    markdown_1.parent_id = background
    markdown_1.order = 1
    markdown_1.save()

    markdown_2.parent_id = background
    markdown_2.order = 2
    markdown_2.save()

    markdown_3.parent_id = background
    markdown_3.order = 3
    markdown_3.save()
    tree_view_1.parent_id = background
    tree_view_1.order = 1
    tree_view_1.save()
    
    markdown_4.parent_id = background
    markdown_4.order = 4
    markdown_4.save()
    tree_view_2.parent_id = background
    tree_view_2.order = 2
    tree_view_2.save()
    markdown_5.parent_id = background
    markdown_5.order = 5
    markdown_5.save()


    # TODO unexpire backgorund
    # unexpire markdown_6, markdown_7, markdown_8, markdown_9
    markdown_6.date_to = None
    markdown_6.save()
    markdown_7.date_to = None
    markdown_7.save()
    markdown_8.date_to = None
    markdown_8.save()
    markdown_9.date_to = None
    markdown_9.save()

    # Delete sections
    section_1.delete()
    section_2.delete()
    section_3.delete()
    section_4.delete()
    sections.delete()


class Migration(migrations.Migration):

    dependencies = [("custom_models", "0020_new_item_types")]

    operations = [migrations.RunPython(reoder_emib_test, rollback_emib_test)]
