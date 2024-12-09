/* eslint-env jest */

import { shallowMount } from "@vue/test-utils";
import AboutView from "../src/views/AboutView.vue";

jest.mock("@/api/index", () => ({
  getCategotiesDataAPI: jest.fn(() =>
    Promise.resolve({
      business: [{ topic: "Business News 1", summary: "Summary 1" }],
      entertainment: [{ topic: "Entertainment News 1", summary: "Summary 1" }],
    })
  ),
  getKeywordsDataAPI: jest.fn(() =>
    Promise.resolve([{ keyword: "keyword1", frequency: 10 }])
  ),
  getSearchDataAPI: jest.fn(() =>
    Promise.resolve({
      item: [
        {
          topic: "Search Result 1",
          summary: "Summary of search result 1",
        },
      ],
    })
  ),
}));

describe("AboutView.vue", () => {
  it("renders correctly", async () => {
    const wrapper = shallowMount(AboutView);
    await wrapper.vm.getData();
    expect(wrapper.exists()).toBe(true);
  });

  it("fetches top keywords on created hook", async () => {
    const wrapper = shallowMount(AboutView);
    await wrapper.vm.getKeywords();
    expect(wrapper.vm.topKeywords.length).toBe(1);
  });
});
