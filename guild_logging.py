from naff import (
    Extension,
    listen,
    Embed,
    BrandColors,
    Message,
    TimestampStyles,
    Role,
    Timestamp,
)
from naff.api.events import (
    MemberUpdate,
    MemberAdd,
    MemberRemove,
    MessageDelete,
    MessageUpdate,
    BaseEvent,
)
from naff.ext.debug_extension import strf_delta


class Logging(Extension):
    ...

    @staticmethod
    def base_embed(event: BaseEvent) -> Embed:
        title = event.resolved_name.replace("on_", "").replace("_", " ").title()
        embed = Embed(title=title, color=BrandColors.BLURPLE)

        return embed

    async def send_embed(self, embed: Embed) -> Message:
        channel = await self.bot.fetch_channel(863554661428494347)
        return await channel.send(embeds=embed)

    @listen()
    async def on_member_update(self, event: MemberUpdate):
        before = event.before
        after = event.after

        if (
            before.display_name == after.display_name and before.roles == after.roles
        ) or (after is None or before is None):
            # filter events
            return None

        emb = self.base_embed(event)
        emb.set_thumbnail(url=after.display_avatar.url)
        emb.set_author(name=after.tag, icon_url=after.display_avatar.url)

        if before.display_name != after.display_name:
            emb.add_field(name="Old Display Name", value=before.display_name)
            emb.add_field(name="New Display Name", value=after.display_name)

        if before.roles != after.roles:
            new_roles: list[Role] = []
            removed_roles: list[Role] = []

            # search for removed roles
            for role in before.roles:
                if role not in after.roles:
                    removed_roles.append(role)

            # search for added roles
            for role in after.roles:
                if role not in before.roles:
                    new_roles.append(role)

            if new_roles:
                emb.add_field(
                    name="New Roles", value="\n".join(r.name for r in new_roles)
                )
            if removed_roles:
                emb.add_field(
                    name="Removed Roles", value="\n".join(r.name for r in removed_roles)
                )

        await self.send_embed(emb)

    @listen()
    async def on_member_add(self, event: MemberAdd):
        emb = self.base_embed(event)
        emb.color = BrandColors.GREEN
        emb.set_author(name=event.member.tag, icon_url=event.member.display_avatar.url)
        emb.add_field(name="📅 Account Creation", value=event.member.created_at)
        emb.add_field(
            name="🕐 Account Age",
            value=event.member.created_at.format(TimestampStyles.RelativeTime),
        )
        emb.set_thumbnail(event.member.display_avatar.url)
        await self.bot.fetch_channel(863553901781712896).send(event.member.mention() + " is exploring the Ruins of Akbadain!")
        await self.send_embed(emb)

    @listen()
    async def on_member_remove(self, event: MemberRemove):
        emb = self.base_embed(event)
        emb.color = BrandColors.BLACK
        emb.set_thumbnail(url=event.member.display_avatar.url)
        emb.set_author(name=event.member.tag, icon_url=event.member.display_avatar.url)

        emb.add_field(name="📅 Account Creation", value=event.member.created_at)
        emb.add_field(
            name="⏰ Left After",
            value=strf_delta(Timestamp.utcnow() - event.member.joined_at),
        )
        await self.bot.fetch_channel(863553901781712896).send(event.member.mention() + " gave up.")
        await self.send_embed(emb)

    @listen()
    async def on_message_edit(self, event: MessageUpdate):
        if not event.before or not event.after:
            return
        if event.before.content == event.after.content:
            return

        emb = self.base_embed(event)
        emb.color = BrandColors.YELLOW
        emb.url = event.before.jump_url
        emb.set_thumbnail(url=event.before.author.display_avatar.url)
        emb.set_author(
            name=event.before.author.tag,
            icon_url=event.before.author.display_avatar.url,
        )

        before_content = event.before.content or "[Empty]"
        if len(before_content) > 1020:
            before_content = before_content[:1020] + "..."
        after_content = event.after.content or "[Empty]"
        if len(after_content) > 1020:
            after_content = after_content[:1020] + "..."
        emb.add_field(name="✏️ Message Edited", value=after_content)
        emb.add_field(
            name="Original Content",
            value=before_content,
        )
        await self.send_embed(emb)

    @listen()
    async def on_message_delete(self, event: MessageDelete):
        print(event.message)
        print(event.message.author)
        print(event.message.author)
        emb = self.base_embed(event)
        emb.color = BrandColors.RED
        emb.set_author(
            name=event.message.author.tag,
            icon_url=event.message.author.avatar.url,
        )

        content = event.message.content or "[Empty]"
        if len(content) > 1020:
            content = content[:1020] + "..."
        emb.add_field(name="🗑️ Message Deleted", value=content)

        if event.message.embeds and (count := len(event.message.embeds)) > 0:
            emb.add_field(name="# Embeds", value=str(count))

        if event.message.attachments and (count := len(event.message.attachments)) > 0:
            emb.add_field(name="# Attachments", value=str(count))

        await self.send_embed(emb)


def setup(bot):
    Logging(bot)
