import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import "../../css/lib/aurora.min.css";
import LOCALIZE from "../../text_resources";
import "../../css/cat-theme.css";
import { LANGUAGES } from "../commons/Translation";
import PopupBox, { BUTTON_TYPE } from "../commons/PopupBox";
import emib_sample_test_example_org_chart_en from "../../images/emib_sample_test_example_org_chart_en.png";
import emib_sample_test_example_org_chart_en_zoomed from "../../images/emib_sample_test_example_org_chart_en.png";
import emib_sample_test_example_org_chart_fr from "../../images/emib_sample_test_example_org_chart_fr.png";
import emib_sample_test_example_org_chart_fr_zoomed from "../../images/emib_sample_test_example_org_chart_fr.png";
import ImageZoom from "react-medium-image-zoom";
import "../../css/react-medium-image-zoom.css";
import { styleConstants } from "./styleConstants.js";

const styles = {
  testImage: {
    width: "100%",
    maxWidth: 600
  },
  button: {
    marginLeft: 5
  }
};

class OrganizationalStructure extends Component {
  static propTypes = {
    // Props from Redux
    currentLanguage: PropTypes.string
  };

  state = {
    showPopupBox: false
  };

  openPopup = () => {
    this.setState({ showPopupBox: true });
  };

  closePopup = () => {
    this.setState({ showPopupBox: false });
  };

  render() {
    const { currentLanguage } = this.props;
    return (
      <div>
        <PopupBox
          show={this.state.showPopupBox}
          handleClose={this.closePopup}
          title={LOCALIZE.emibTest.background.organizationalStructure.dialog.title}
          description={
            <div>
              <ul>
                <li>
                  Jenna Icard - President
                  <ul>
                    <li>
                      Amari Kinsler - Corporate Affairs Director
                      <ul>
                        <li>Marc Sheridan - Human Resources Manager</li>
                        <li>Bob McNutt - Finance Manager</li>
                        <li>Lana Hussad - Information Technology Manager</li>
                      </ul>
                    </li>
                    <li>Geneviève Bédard - Research and Innovations Director</li>
                    <li>Bartosz Greco - Program Development Director</li>
                    <li>
                      Nancy Ward - Services and Communications Director
                      <ul>
                        <li>Claude Huard - Quality Assurance Manager (You)</li>
                        <li>Haydar Kalil - Services and Support Manager</li>
                        <li>Geoffrey Hamma - Audits Manager</li>
                        <li>Lucy Trang - E-Training Manager</li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
          }
          rightButtonType={BUTTON_TYPE.secondary}
          rightButtonTitle={LOCALIZE.commons.close}
        />
        <div>
          <h2>{LOCALIZE.emibTest.background.organizationalStructure.title}</h2>
          <div>
            <p style={styleConstants.instuctions.p}>
              {LOCALIZE.emibTest.background.organizationalStructure.description}
            </p>
            <p style={styleConstants.instuctions.p}>
              <span className="font-weight-bold">
                {LOCALIZE.emibTest.background.organizationalStructure.para1Title}
              </span>
              {LOCALIZE.emibTest.background.organizationalStructure.para1}
            </p>
            <p style={styleConstants.instuctions.p}>
              <span className="font-weight-bold">
                {LOCALIZE.emibTest.background.organizationalStructure.para2Title}
              </span>
              {LOCALIZE.emibTest.background.organizationalStructure.para2}
            </p>
            <p style={styleConstants.instuctions.p}>
              <span className="font-weight-bold">
                {LOCALIZE.emibTest.background.organizationalStructure.para3Title}
              </span>
              {LOCALIZE.emibTest.background.organizationalStructure.para3}
            </p>
            <p style={styleConstants.instuctions.p}>
              <span className="font-weight-bold">
                {LOCALIZE.emibTest.background.organizationalStructure.para4Title}
              </span>
              {LOCALIZE.emibTest.background.organizationalStructure.para4}
            </p>
            <p style={styleConstants.instuctions.p}>
              {currentLanguage === LANGUAGES.english && (
                <ImageZoom
                  image={{
                    src: emib_sample_test_example_org_chart_en,
                    alt: LOCALIZE.emibTest.background.organizationalStructure.orgChart.desciption,
                    style: styles.testImage,
                    className: "ie-zoom-cursor"
                  }}
                  zoomImage={{
                    src: emib_sample_test_example_org_chart_en_zoomed,
                    alt: LOCALIZE.emibTest.background.organizationalStructure.orgChart.desciption,
                    className: "ie-zoom-cursor"
                  }}
                />
              )}
              {currentLanguage === LANGUAGES.french && (
                <ImageZoom
                  image={{
                    src: emib_sample_test_example_org_chart_fr,
                    alt: LOCALIZE.emibTest.background.organizationalStructure.orgChart.desciption,
                    style: styles.testImage,
                    className: "ie-zoom-cursor"
                  }}
                  zoomImage={{
                    src: emib_sample_test_example_org_chart_fr_zoomed,
                    alt: LOCALIZE.emibTest.background.organizationalStructure.orgChart.desciption,
                    className: "ie-zoom-cursor"
                  }}
                />
              )}
            </p>
            <button
              id="org-image-description"
              onClick={this.openPopup}
              className="btn btn-secondary"
              style={styles.button}
            >
              {LOCALIZE.emibTest.background.organizationalStructure.orgChart.link}
            </button>
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

export default connect(
  mapStateToProps,
  null
)(OrganizationalStructure);
