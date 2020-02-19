
from odoo import models, fields, api
from odoo import tools


class FunnelReport(models.Model):
    _name = "funnel.report"
    _description = "FunnelReport"

    date = fields.Date(readonly=True)
    crm_team_id = fields.Many2one('crm.team', 'Salesteam')
    user_id = fields.Many2one('res.users', 'Salesperson', default=lambda self: self.env.user)
    achieved_calls = fields.Float('Achieved')
    target_calls = fields.Float('Target')
    calls = fields.Char('AMJ 2017')

    # def init(self):
    #     tools.drop_view_if_exists(self.env.cr, self._table)
    #
    #     self.env.cr.execute("""
    #             create or replace view funnel_dates_cal as (
    #                select dates::date,extract (month from dates) as month from generate_series(date_trunc('month', current_date), date_trunc('month',
    #                 current_date)+'1month'::interval-'1day'::interval, '1 day'::interval) dates)
    #         """)
    #
    #     # calls
    #     tools.drop_view_if_exists(self._cr, "calls_count")
    #     self._cr.execute(""" create or replace view calls_count as (
    #                  select d.date, count(se.id) as achieved_calls,se.user_id,dates FROM (
    #                  select to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')
    #                  AS date,
    #                   to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')::date
    #                  AS dates
    #                  FROM generate_series(0, 365, 1)
    #                  AS offs
    #                  ) d
    #                  JOIN crm_phonecall se
    #                  ON (d.date=to_char(date_trunc('day', se.date), 'YYYY-MM-DD'))
    #                  where se.name='call' and extract(month from se.date) = extract(month from current_date)
    #                  GROUP BY d.date,se.user_id,dates)""")
    #
    #     # funnel
    #     tools.drop_view_if_exists(self._cr, "sale_amount_funnel_month")
    #     self.env.cr.execute("""create or replace view sale_amount_funnel_month as (
    #         select case when extract(month from current_date)=1 then fl.jan
    #                     when extract(month from current_date)=2 then fl.feb
    #                     when extract(month from current_date)=3 then fl.mar
    #                     when extract(month from current_date)=4 then fl.apr
    #                     when extract(month from current_date)=5 then fl.may
    #                     when extract(month from current_date)=6 then fl.jun
    #                     when extract(month from current_date)=7 then fl.jul
    #                     when extract(month from current_date)=8 then fl.aug
    #                     when extract(month from current_date)=9 then fl.sep
    #                     when extract(month from current_date)=10 then fl.octt
    #                     when extract(month from current_date)=11 then fl.nov
    #                     when extract(month from current_date)=12 then fl.dec
    #                end as mont, fl.user_id
    #         from funnel_line as fl
    #         left join sale_order as so on so.user_id =  fl.user_id
    #         )""")
    #
    #     tools.drop_view_if_exists(self._cr, "sale_amount_funnel_count")
    #     self.env.cr.execute("""create or replace view sale_amount_funnel_count as (
    #         SELECT d.date, count(se.id) as achieved_calls,se.user_id,dates,sum(se.amount_untaxed) as amount_untaxed FROM (
    #         select to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')
    #         AS date,
    #         to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')::date
    #         AS dates
    #         FROM generate_series(0, 365, 1)
    #         AS offs
    #         ) d
    #         JOIN sale_order se
    #         ON (d.date=to_char(date_trunc('day', se.date_order), 'YYYY-MM-DD'))
    #         where se.state='draft' and extract(month from se.date_order) = extract(month from current_date)
    #         GROUP BY d.date,se.user_id,dates)""")
    #
    #     # order booked
    #     tools.drop_view_if_exists(self._cr, "sale_amount_order_month")
    #     self.env.cr.execute("""create or replace view sale_amount_order_month as (
    #         select case when extract(month from current_date)=1 then obl.jan
    #                     when extract(month from current_date)=2 then obl.feb
    #                     when extract(month from current_date)=3 then obl.mar
    #                     when extract(month from current_date)=4 then obl.apr
    #                     when extract(month from current_date)=5 then obl.may
    #                     when extract(month from current_date)=6 then obl.jun
    #                     when extract(month from current_date)=7 then obl.jul
    #                     when extract(month from current_date)=8 then obl.aug
    #                     when extract(month from current_date)=9 then obl.sep
    #                     when extract(month from current_date)=10 then obl.octt
    #                     when extract(month from current_date)=11 then obl.nov
    #                     when extract(month from current_date)=12 then obl.dec
    #                end as mont, obl.user_id
    #         from booked_line as obl
    #         left join sale_order as so on so.user_id =  obl.user_id
    #         )""")
    #
    #     tools.drop_view_if_exists(self._cr, "sale_amount_order_count")
    #     self.env.cr.execute("""create or replace view sale_amount_order_count as (
    #         SELECT d.date, count(se.id) as achieved_calls,se.user_id,dates,sum(se.amount_untaxed) as amount_untaxed FROM (
    #         select to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')
    #         AS date,
    #         to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')::date
    #         AS dates
    #         FROM generate_series(0, 365, 1)
    #         AS offs
    #         ) d
    #         JOIN sale_order se
    #         ON (d.date=to_char(date_trunc('day', se.date_order), 'YYYY-MM-DD'))
    #         where se.state='done' and extract(month from se.date_order) = extract(month from current_date)
    #         GROUP BY d.date,se.user_id,dates)""")
    #
    #     # tl billing
    #     tools.drop_view_if_exists(self._cr, "tl_billing_sale_amount_order_month")
    #     self.env.cr.execute("""create or replace view tl_billing_sale_amount_order_month as (
    #         select case when extract(month from current_date)=1 then tbl.jan
    #                     when extract(month from current_date)=2 then tbl.feb
    #                     when extract(month from current_date)=3 then tbl.mar
    #                     when extract(month from current_date)=4 then tbl.apr
    #                     when extract(month from current_date)=5 then tbl.may
    #                     when extract(month from current_date)=6 then tbl.jun
    #                     when extract(month from current_date)=7 then tbl.jul
    #                     when extract(month from current_date)=8 then tbl.aug
    #                     when extract(month from current_date)=9 then tbl.sep
    #                     when extract(month from current_date)=10 then tbl.octt
    #                     when extract(month from current_date)=11 then tbl.nov
    #                     when extract(month from current_date)=12 then tbl.dec
    #                end as mont, tbl.user_id
    #         from tl_billing_line as tbl
    #         left join sale_order as so on so.user_id =  tbl.user_id
    #         )""")
    #
    #     tools.drop_view_if_exists(self._cr, "tl_billing_sale_amount_order_count")
    #     self.env.cr.execute("""create or replace view tl_billing_sale_amount_order_count as (
    #         SELECT d.date, count(ai.id) as achieved_calls,ai.user_id,dates,sum(ai.amount_untaxed) as amount_untaxed FROM (
    #         select to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')
    #         AS date,
    #         to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')::date
    #         AS dates
    #         FROM generate_series(0, 365, 1)
    #         AS offs
    #         ) d
    #         JOIN account_invoice as ai
    #         ON (d.date=to_char(date_trunc('day', ai.date_invoice), 'YYYY-MM-DD'))
    #         where ai.state in ('open','paid') and extract(month from ai.date_invoice) = extract(month from current_date)
    #         GROUP BY d.date,ai.user_id,dates)""")
    #
    #     # bl billing
    #     tools.drop_view_if_exists(self._cr, "bl_billing_sale_amount_order_month")
    #     self.env.cr.execute("""create or replace view bl_billing_sale_amount_order_month as (
    #         select case when extract(month from current_date)=1 then bbl.jan
    #                     when extract(month from current_date)=2 then bbl.feb
    #                     when extract(month from current_date)=3 then bbl.mar
    #                     when extract(month from current_date)=4 then bbl.apr
    #                     when extract(month from current_date)=5 then bbl.may
    #                     when extract(month from current_date)=6 then bbl.jun
    #                     when extract(month from current_date)=7 then bbl.jul
    #                     when extract(month from current_date)=8 then bbl.aug
    #                     when extract(month from current_date)=9 then bbl.sep
    #                     when extract(month from current_date)=10 then bbl.octt
    #                     when extract(month from current_date)=11 then bbl.nov
    #                     when extract(month from current_date)=12 then bbl.dec
    #                end as mont, bbl.user_id
    #         from bl_billing_line as bbl
    #         left join sale_order as so on so.user_id =  bbl.user_id
    #         )""")
    #
    #     tools.drop_view_if_exists(self._cr, "bl_billing_sale_amount_order_count")
    #     self.env.cr.execute("""create or replace view bl_billing_sale_amount_order_count as (
    #                     SELECT d.date, count(se.id),se.user_id,dates,se.amount_untaxed,sum(brl.purchase_unit_price) as purchase_unit_price,
    #                     sum(brl.purchase_unit_price/100)*brl.margin_percentage+sum(brl.purchase_unit_price) as achieved_calls,
    #                     brl.margin_percentage FROM
    #                     ( select to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')
    #                     AS date,
    #                     to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')::date
    #                     AS dates
    #                     FROM generate_series(0, 365, 1)
    #                     AS offs
    #                     ) d
    #                     JOIN sale_order se
    #                     left join purchase_requisition as pr on pr.id = se.tender_id
    #                     left join bid_received_line as brl on brl.tender_id = pr.id
    #                     ON (d.date=to_char(date_trunc('day', se.date_order), 'YYYY-MM-DD'))
    #                     where se.state='done' and extract(month from se.date_order) = extract(month from current_date) and pr.id = se.tender_id
    #                     GROUP BY d.date,se.user_id,dates,se.amount_untaxed,brl.margin_percentage)""")
    #
    #     # payment receive
    #     tools.drop_view_if_exists(self._cr, "payment_receive_month")
    #     self.env.cr.execute("""create or replace view payment_receive_month as (
    #         select case when extract(month from current_date)=1 then prl.jan
    #                     when extract(month from current_date)=2 then prl.feb
    #                     when extract(month from current_date)=3 then prl.mar
    #                     when extract(month from current_date)=4 then prl.apr
    #                     when extract(month from current_date)=5 then prl.may
    #                     when extract(month from current_date)=6 then prl.jun
    #                     when extract(month from current_date)=7 then prl.jul
    #                     when extract(month from current_date)=8 then prl.aug
    #                     when extract(month from current_date)=9 then prl.sep
    #                     when extract(month from current_date)=10 then prl.octt
    #                     when extract(month from current_date)=11 then prl.nov
    #                     when extract(month from current_date)=12 then prl.dec
    #                end as mont, prl.user_id
    #         from pay_receive_line as prl
    #         left join account_invoice as ai on ai.user_id =  prl.user_id
    #         )""")
    #
    #     tools.drop_view_if_exists(self._cr, "payment_receive_count")
    #     self.env.cr.execute("""create or replace view payment_receive_count as (
    #         SELECT d.date, count(ai.id) as achieved_calls,ai.user_id,dates,sum(ai.amount_total-ai.residual) as amount_received FROM (
    #         select to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')
    #         AS date,
    #         to_char(date_trunc('day', (current_date - offs)), 'YYYY-MM-DD')::date
    #         AS dates
    #         FROM generate_series(0, 365, 1)
    #         AS offs
    #         ) d
    #         JOIN account_invoice ai
    #         ON (d.date=to_char(date_trunc('day', ai.date_invoice), 'YYYY-MM-DD'))
    #         where ai.state='open' and ai.type='out_invoice' and extract(month from ai.date_invoice) = extract(month from current_date)
    #         GROUP BY d.date,ai.user_id,dates)""")
    #
    #     # main query
    #     tools.drop_view_if_exists(self._cr, self._table)
    #     self.env.cr.execute(""" CREATE view %s as
    #
    #                 select id,dates as date,call_count/7 as target_calls,sum(achieved_calls) as achieved_calls,user_id,crm_team_id,calls
    #                                 from
    #                                 (
    #                                 select dr.dates,tl.user_id,tl.calls,tl.call_count,
    #                                 DATE_PART('days',
    #                                          DATE_TRUNC('month', dr.dates)
    #                                  + '1 MONTH'::INTERVAL
    #                                  - '1 DAY'::INTERVAL
    #                                      ) as days,tc.achieved_calls,ru.sale_team_id as crm_team_id,tl.id
    #                                 from target_line as tl
    #                                 left join funnel_dates_cal as dr on extract(month from dates) = extract(month from current_date)
    #                                 left join calls_count as tc on tc.dates = dr.dates and tc.user_id = tl.user_id
    #                                 left join res_users ru on ru.id = tl.user_id
    #                                 left join crm_team ct on ct.id = ru.sale_team_id
    #                                 )temp
    #                                 group by temp.id,temp.call_count/7,temp.user_id,temp.crm_team_id,temp.days,temp.dates,temp.calls
    #
    #                                 UNION ALL
    #
    #
    #                 select id ,dates as date,mont/days as target_calls,achieved_calls,user_id,crm_team_id,funnel
    #                                 from
    #                                 (
    #                                 select dr.dates,tl.user_id,tl.funnel,
    #                                 DATE_PART('days',
    #                                          DATE_TRUNC('month', dr.dates)
    #                                  + '1 MONTH'::INTERVAL
    #                                  - '1 DAY'::INTERVAL
    #                                      ) as days,tc.amount_untaxed as achieved_calls,ru.sale_team_id as crm_team_id,tl.id,ufc.mont
    #
    #                                 from funnel_line as tl
    #                                 left join funnel_dates_cal as dr on extract(month from dates) = extract(month from current_date)
    #                                 left join sale_amount_funnel_count as tc on tc.dates = dr.dates and tc.user_id = tl.user_id
    #                                 left join sale_amount_funnel_month as ufc on ufc.user_id = tl.user_id
    #                                 left join res_users ru on ru.id = tl.user_id
    #                                 left join crm_team ct on ct.id = ru.sale_team_id
    #                                 )temp
    #                                 group by temp.id,temp.mont/days,temp.user_id,temp.crm_team_id,temp.days,temp.dates,temp.achieved_calls,temp.funnel
    #
    #                                 UNION ALL
    #
    #
    #                 select id ,dates as date,mont/days as target_calls,achieved_calls,user_id,crm_team_id,order_booked
    #                                 from
    #                                 (
    #                                 select dr.dates,tl.user_id,tl.order_booked,
    #                                 DATE_PART('days',
    #                                          DATE_TRUNC('month', dr.dates)
    #                                  + '1 MONTH'::INTERVAL
    #                                  - '1 DAY'::INTERVAL
    #                                      ) as days,tc.amount_untaxed as achieved_calls,ru.sale_team_id as crm_team_id,tl.id,ufc.mont
    #
    #                                 from booked_line as tl
    #                                 left join funnel_dates_cal as dr on extract(month from dates) = extract(month from current_date)
    #                                 left join sale_amount_order_count as tc on tc.dates = dr.dates and tc.user_id = tl.user_id
    #                                 left join sale_amount_order_month as ufc on ufc.user_id = tl.user_id
    #                                 left join res_users ru on ru.id = tl.user_id
    #                                 left join crm_team ct on ct.id = ru.sale_team_id
    #                                 )temp
    #                                 group by temp.id,temp.mont/days,temp.user_id,temp.crm_team_id,temp.days,temp.dates,temp.achieved_calls,temp.order_booked
    #
    #                                 UNION ALL
    #
    #
    #                 select id ,dates as date,mont/days as target_calls,achieved_calls,user_id,crm_team_id,tl_billing
    #                                 from
    #                                 (
    #                                 select dr.dates,tl.user_id,tl.tl_billing,
    #                                 DATE_PART('days',
    #                                          DATE_TRUNC('month', dr.dates)
    #                                  + '1 MONTH'::INTERVAL
    #                                  - '1 DAY'::INTERVAL
    #                                      ) as days,tc.amount_untaxed as achieved_calls,ru.sale_team_id as crm_team_id,tl.id,ufc.mont
    #
    #                                 from tl_billing_line as tl
    #                                 left join funnel_dates_cal as dr on extract(month from dates) = extract(month from current_date)
    #                                 left join tl_billing_sale_amount_order_count as tc on tc.dates = dr.dates and tc.user_id = tl.user_id
    #                                 left join tl_billing_sale_amount_order_month as ufc on ufc.user_id = tl.user_id
    #                                 left join res_users ru on ru.id = tl.user_id
    #                                 left join crm_team ct on ct.id = ru.sale_team_id
    #                                 )temp
    #                                 group by temp.id,temp.mont/days,temp.user_id,temp.crm_team_id,temp.days,temp.dates,temp.achieved_calls,temp.tl_billing
    #
    #                                 UNION ALL
    #
    #
    #                 select id ,dates as date,mont/days as target_calls,achieved_calls,user_id,crm_team_id,bl_billing
    #                                 from
    #                                 (
    #                                 select dr.dates,tl.user_id,tl.bl_billing,
    #                                 DATE_PART('days',
    #                                          DATE_TRUNC('month', dr.dates)
    #                                  + '1 MONTH'::INTERVAL
    #                                  - '1 DAY'::INTERVAL
    #                                      ) as days,tc.achieved_calls as achieved_calls,ru.sale_team_id as crm_team_id,tl.id,ufc.mont
    #
    #                                 from bl_billing_line as tl
    #                                 left join funnel_dates_cal as dr on extract(month from dates) = extract(month from current_date)
    #                                 left join bl_billing_sale_amount_order_count as tc on tc.dates = dr.dates and tc.user_id = tl.user_id
    #                                 left join bl_billing_sale_amount_order_month as ufc on ufc.user_id = tl.user_id
    #                                 left join res_users ru on ru.id = tl.user_id
    #                                 left join crm_team ct on ct.id = ru.sale_team_id
    #                                 )temp
    #                                 group by temp.id,temp.mont/days,temp.user_id,temp.crm_team_id,temp.days,temp.dates,temp.achieved_calls,temp.bl_billing
    #
    #                                 UNION ALL
    #
    #                 select id ,dates as date,mont/days as target_calls,achieved_calls,user_id,crm_team_id,pay_receive
    #                                 from
    #                                 (
    #                                 select dr.dates,tl.user_id,tl.pay_receive,
    #                                 DATE_PART('days',
    #                                          DATE_TRUNC('month', dr.dates)
    #                                  + '1 MONTH'::INTERVAL
    #                                  - '1 DAY'::INTERVAL
    #                                      ) as days,tc.amount_received as achieved_calls,ru.sale_team_id as crm_team_id,tl.id,ufc.mont
    #
    #                                 from pay_receive_line as tl
    #                                 left join funnel_dates_cal as dr on extract(month from dates) = extract(month from current_date)
    #                                 left join payment_receive_count as tc on tc.dates = dr.dates and tc.user_id = tl.user_id
    #                                 left join payment_receive_month as ufc on ufc.user_id = tl.user_id
    #                                 left join res_users ru on ru.id = tl.user_id
    #                                 left join crm_team ct on ct.id = ru.sale_team_id
    #                                 )temp
    #                                 group by temp.id,temp.mont/days,temp.user_id,temp.crm_team_id,temp.days,temp.dates,temp.achieved_calls,temp.pay_receive
    #
    #                         """ % (self._table,))