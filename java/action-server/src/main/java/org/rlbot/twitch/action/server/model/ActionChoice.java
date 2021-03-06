package org.rlbot.twitch.action.server.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.rlbot.twitch.action.server.model.BotAction;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * ActionChoice
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2020-06-13T09:35:18.293-07:00[America/Los_Angeles]")
public class ActionChoice   {
  @JsonProperty("action")
  private BotAction action = null;

  @JsonProperty("entityName")
  private String entityName = null;

  public ActionChoice action(BotAction action) {
    this.action = action;
    return this;
  }

  /**
   * Get action
   * @return action
  **/
  @ApiModelProperty(value = "")
  
    @Valid
    public BotAction getAction() {
    return action;
  }

  public void setAction(BotAction action) {
    this.action = action;
  }

  public ActionChoice entityName(String entityName) {
    this.entityName = entityName;
    return this;
  }

  /**
   * The name of the bot or script that this action is associated with.
   * @return entityName
  **/
  @ApiModelProperty(example = "SomeBot", value = "The name of the bot or script that this action is associated with.")
  
    public String getEntityName() {
    return entityName;
  }

  public void setEntityName(String entityName) {
    this.entityName = entityName;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ActionChoice actionChoice = (ActionChoice) o;
    return Objects.equals(this.action, actionChoice.action) &&
        Objects.equals(this.entityName, actionChoice.entityName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(action, entityName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ActionChoice {\n");
    
    sb.append("    action: ").append(toIndentedString(action)).append("\n");
    sb.append("    entityName: ").append(toIndentedString(entityName)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}
