import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import ReactMarkdown from "react-markdown";
import LOCALIZE from "../../text_resources";
import { LANGUAGES } from "../../modules/LocalizeRedux";
import PopupBox, { BUTTON_TYPE } from "../commons/PopupBox";
import emib_sample_test_example_team_chart_en from "../../images/emib_sample_test_example_team_chart_en.png";
import emib_sample_test_example_team_chart_en_zoomed from "../../images/emib_sample_test_example_team_chart_en.png";
import emib_sample_test_example_team_chart_fr from "../../images/emib_sample_test_example_team_chart_fr.png";
import emib_sample_test_example_team_chart_fr_zoomed from "../../images/emib_sample_test_example_team_chart_fr.png";
import ImageZoom from "react-medium-image-zoom";
import "../../css/react-medium-image-zoom.css";
import TreeNode from "../commons/TreeNode";
import { getTestQuestions } from "../../modules/LoadTestContentRedux";
import { TEST_DEFINITION } from "../../testDefinition";
import { processTreeContent } from "../../helpers/transformations";

const styles = {
  testImage: {
    width: "100%",
    maxWidth: 600
  },
  button: {
    marginLeft: 5
  }
};

class TeamInformation extends Component {
  static propTypes = {
    // Props from Redux
    currentLanguage: PropTypes.string,
    getTestQuestions: PropTypes.func
  };

  state = {
    showPopupBox: false,
    isLoadingComplete: false,
    markdown_section1_en: "",
    markdown_section1_fr: "",
    markdown_section2_en: "",
    markdown_section2_fr: "",
    popupMarkdownTitle_en: "",
    popupMarkdownTitle_fr: "",
    popupMarkdownDescription_en: "",
    popupMarkdownDescription_fr: "",
    treeViewContent_en: [],
    treeViewContent_fr: []
  };

  openPopup = () => {
    this.setState({ showPopupBox: true });
  };

  closePopup = () => {
    this.setState({ showPopupBox: false });
  };

  // loads the markdown content (english and french versions)
  componentWillMount = () => {
    this.props.getTestQuestions(TEST_DEFINITION.emib.sampleTest).then(response => {
      // Save the team information markdown content in local states.
      this.setState({
        markdown_section1_en: response.background.en.background[0].markdown[3].text,
        markdown_section1_fr: response.background.fr.background[0].markdown[3].text,
        markdown_section2_en: response.background.en.background[0].markdown[4].text,
        markdown_section2_fr: response.background.fr.background[0].markdown[4].text,
        popupMarkdownTitle_en: response.background.en.background[0].markdown[7].text,
        popupMarkdownTitle_fr: response.background.fr.background[0].markdown[7].text,
        popupMarkdownDescription_en: response.background.en.background[0].markdown[8].text,
        popupMarkdownDescription_fr: response.background.fr.background[0].markdown[8].text,
        treeViewContent_en:
          response.background.en.background[0].tree_view[1].team_information_tree_child,
        treeViewContent_fr:
          response.background.fr.background[0].tree_view[1].team_information_tree_child,
        isLoadingComplete: true
      });
    });
  };

  render() {
    const { currentLanguage } = this.props;
    const { treeViewContent_en, treeViewContent_fr } = this.state;

    let treeView = [];
    // waiting for tree view content data loading
    if (this.state.isLoadingComplete) {
      treeView = processTreeContent(
        currentLanguage,
        treeViewContent_en,
        treeViewContent_fr,
        "team_information_tree_child"
      );
    }

    return (
      <div>
        <PopupBox
          show={this.state.showPopupBox}
          handleClose={this.closePopup}
          // only using the states here (without markdown), since the title must be a string
          title={
            this.props.currentLanguage === LANGUAGES.english
              ? this.state.popupMarkdownTitle_en
              : this.state.popupMarkdownTitle_fr
          }
          description={
            <div>
              {this.props.currentLanguage === LANGUAGES.english && (
                <ReactMarkdown source={this.state.popupMarkdownDescription_en} />
              )}
              {this.props.currentLanguage === LANGUAGES.french && (
                <ReactMarkdown source={this.state.popupMarkdownDescription_fr} />
              )}
              <TreeNode nodes={treeView} />
            </div>
          }
          rightButtonType={BUTTON_TYPE.secondary}
          rightButtonTitle={LOCALIZE.commons.close}
        />
        <div>
          {this.props.currentLanguage === LANGUAGES.english && (
            <ReactMarkdown source={this.state.markdown_section1_en} />
          )}
          {this.props.currentLanguage === LANGUAGES.french && (
            <ReactMarkdown source={this.state.markdown_section1_fr} />
          )}
          <div>
            <p>
              {currentLanguage === LANGUAGES.english && (
                <ImageZoom
                  longdesc="#team-image-description"
                  image={{
                    src: emib_sample_test_example_team_chart_en,
                    alt: LOCALIZE.emibTest.background.teamInformation.teamChart.desciption,
                    style: styles.testImage,
                    className: "ie-zoom-cursor"
                  }}
                  zoomImage={{
                    src: emib_sample_test_example_team_chart_en_zoomed,
                    alt: LOCALIZE.emibTest.background.teamInformation.teamChart.desciption,
                    className: "ie-zoom-cursor"
                  }}
                />
              )}
              {currentLanguage === LANGUAGES.french && (
                <ImageZoom
                  longdesc="#team-image-description"
                  image={{
                    src: emib_sample_test_example_team_chart_fr,
                    alt: LOCALIZE.emibTest.background.teamInformation.teamChart.desciption,
                    style: styles.testImage,
                    className: "ie-zoom-cursor"
                  }}
                  zoomImage={{
                    src: emib_sample_test_example_team_chart_fr_zoomed,
                    alt: LOCALIZE.emibTest.background.teamInformation.teamChart.desciption,
                    className: "ie-zoom-cursor"
                  }}
                />
              )}
            </p>
            <button
              id="team-image-description"
              onClick={this.openPopup}
              className="btn btn-secondary"
              style={styles.button}
              aria-label={LOCALIZE.emibTest.background.teamInformation.teamChart.ariaLabel}
            >
              {LOCALIZE.emibTest.background.teamInformation.teamChart.link}
            </button>
          </div>
          <div>
            {this.props.currentLanguage === LANGUAGES.english && (
              <ReactMarkdown source={this.state.markdown_section2_en} />
            )}
            {this.props.currentLanguage === LANGUAGES.french && (
              <ReactMarkdown source={this.state.markdown_section2_fr} />
            )}
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return {
    currentLanguage: state.localize.language
  };
};

const mapDispatchToProps = dispatch =>
  bindActionCreators(
    {
      getTestQuestions
    },
    dispatch
  );

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(TeamInformation);
