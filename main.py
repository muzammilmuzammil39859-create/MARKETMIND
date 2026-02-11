import streamlit as st

st.set_page_config(page_title="MarketMate Pro", layout="wide")

st.title("📈 MarketMate Pro – Offline AI Marketing Agent")
st.caption("Professional Marketing Strategy Generator (Offline Demo Version)")

# ---------------- STRATEGY ENGINE ---------------- #

def generate_full_strategy(name, business_type, location, budget, goal, audience):

    report = f"""
===============================
📊 BUSINESS ANALYSIS REPORT
===============================

Business Name: {name}
Industry: {business_type}
Location: {location}
Target Audience: {audience}
Marketing Budget: ₹{budget}
Primary Goal: {goal}

"""

    # SWOT Section
    report += "\n🔍 SWOT ANALYSIS\n"

    report += """
Strengths:
- Local market opportunity
- Direct customer engagement potential

Weaknesses:
- Limited brand awareness
- Budget constraints (if applicable)

Opportunities:
- Social media growth
- Influencer collaborations
- Digital advertising expansion

Threats:
- Strong competitors
- Changing customer trends
"""

    # Strategy Section
    report += "\n🎯 MARKETING STRATEGY\n"

    if goal == "Increase Sales":
        report += """
- Run targeted social media ads
- Offer limited-time discounts
- Use WhatsApp for direct promotions
- Upsell to existing customers
"""
    elif goal == "Brand Awareness":
        report += """
- Create Instagram reels & YouTube Shorts
- Collaborate with micro-influencers
- Sponsor local events
- Run reach-focused ad campaigns
"""
    elif goal == "Product Launch":
        report += """
- Teaser campaign before launch
- Influencer unboxing content
- Launch day live event
- Early bird offers
"""
    else:
        report += """
- Loyalty programs
- Email marketing
- Retargeting campaigns
- Customer feedback strategy
"""

    # Budget Allocation
    report += "\n💰 BUDGET ALLOCATION PLAN\n"

    if budget > 100000:
        report += """
40% Paid Ads
20% Influencer Marketing
20% Branding & Design
20% Automation Tools
"""
    elif budget > 40000:
        report += """
50% Social Media Ads
20% Content Creation
20% Local Promotions
10% CRM Tools
"""
    else:
        report += """
70% Organic Social Media
20% Referral Marketing
10% Basic Promotions
"""

    # 30-Day Plan
    report += "\n📅 30-DAY ACTION PLAN\n"

    report += """
Week 1:
- Market research & competitor analysis
- Content planning

Week 2:
- Launch ad campaigns
- Start influencer outreach

Week 3:
- Monitor ad performance
- Optimize targeting

Week 4:
- Analyze results
- Scale winning campaigns
"""

    report += "\n🚀 AI Conclusion:\n"
    report += "Focus on consistent branding, targeted digital ads, and measurable campaigns for maximum ROI.\n"

    return report


# ---------------- USER INTERFACE ---------------- #

st.header("🏢 Enter Business Details")

col1, col2 = st.columns(2)

with col1:
    business_name = st.text_input("Business Name")
    business_type = st.text_input("Industry Type")
    location = st.text_input("Location")

with col2:
    budget = st.number_input("Marketing Budget (₹)", min_value=0)
    goal = st.selectbox(
        "Marketing Goal",
        ["Increase Sales", "Brand Awareness", "Product Launch", "Customer Retention"]
    )
    audience = st.text_input("Target Audience (e.g., Students, Families, Working Professionals)")

# ---------------- RUN AGENT ---------------- #

if st.button("🤖 Generate Professional Marketing Report"):

    if business_name == "" or business_type == "" or location == "" or audience == "":
        st.warning("Please fill all required details.")
    else:
        report = generate_full_strategy(
            business_name,
            business_type,
            location,
            budget,
            goal,
            audience
        )

        st.subheader("📑 Generated Marketing Strategy Report")
        st.text(report)

        st.success("✅ AI Strategy Generated Successfully")



