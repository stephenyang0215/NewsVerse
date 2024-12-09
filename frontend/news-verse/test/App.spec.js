/* eslint-env jest */

import { shallowMount } from "@vue/test-utils";
import App from "../src/App.vue";

describe("App.vue", () => {
  it("renders correctly", () => {
    const wrapper = shallowMount(App);
    expect(wrapper.exists()).toBe(true);
  });

  it("contains the title 'News Verse'", () => {
    const wrapper = shallowMount(App);
    expect(wrapper.find(".title").text()).toBe("News Verse");
  });
});
