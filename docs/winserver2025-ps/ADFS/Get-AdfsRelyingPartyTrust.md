---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsRelyingPartyTrust
---

# Get-AdfsRelyingPartyTrust

## 摘要
获取联邦服务的依赖方信任信息。

## 语法

### RelyingPartyName（默认值）
```
Get-AdfsRelyingPartyTrust [[-Name] <String[]>] [<CommonParameters>]
```

### 标识符
```
Get-AdfsRelyingPartyTrust [-Identifier] <String[]> [<CommonParameters>]
```

### PrefixIdentifier
```
Get-AdfsRelyingPartyTrust [-PrefixIdentifier] <String> [<CommonParameters>]
```

## 描述
`Get-AdfsRelyingPartyTrust` cmdlet 可以获取联邦服务（Federation Service）的依赖方信任关系信息。您可以不带任何参数使用此 cmdlet 来获取所有的依赖方信任对象。

## 示例

### 示例 1：通过名称获取依赖方信任的属性设置
```
PS C:\> Get-AdfsRelyingPartyTrust -Name "FabrikamApp"
```

这个命令用于获取名为“FabrikamApp”的依赖方信任（relying party trust）的属性设置。

### 示例 2：使用标识符获取依赖方信任的属性设置
```
PS C:\> Get-AdfsRelyingPartyTrust -Identifier "https://FabrikamApp.CentralServer.org"
```

此命令用于获取标识符为 `https://FabrikamApp.CentralServer.org` 的依赖方信任（relying party trust）的属性设置。

### 示例 3：获取已更新的依赖方信任关系的属性设置
```
PS C:\> Get-AdfsRelyingPartyTrust | Where-Object{ $_.LastUpdateTime -le (get-date).subtract((new-timespan -hours 24))}
```

此命令用于获取在过去 24 小时内已更新的依赖方信任（relying party trusts）的属性设置信息。

## 参数

### -Identifier
指定一个包含依赖方信任标识符的唯一标识符数组以供获取。

```yaml
Type: String[]
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定要获取的依赖方信任（relying party trust）的显示名称。

```yaml
Type: String[]
Parameter Sets: RelyingPartyName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PrefixIdentifier
指定要获取的依赖方信任的前缀标识符。联合服务（Federation Service）使用前缀匹配来支持通配符类型的过滤，并根据特定的前缀URL进行匹配操作。该服务通过字符串数据类型的评估来进行匹配；匹配时不区分大小写。

```yaml
Type: String
Parameter Sets: PrefixIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *Identifier*、*Name* 和 *PrefixIdentifier* 参数被接收。

## 输出

### Microsoft.IdentityServer.PowerShellResources.RelyingPartyTrust

返回一个或多个 RelyingPartyTrust 对象，这些对象代表联合服务（Federation Service）的依赖方信任资源。

## 备注
* If no *Identifier* parameter is provided, the cmdlet returns all **RelyingPartyTrust** objects. A relying party in Active Directory Federation Services (AD FS) is an organization in which Web servers that host one or more Web-based applications reside. Tokens and Information Cards that originate from a claims provider can then be presented and ultimately consumed by the Web-based resources that are located in the relying party organization. When AD FS is configured in the role of the relying party, it acts as a partner that trusts a claims provider to authenticate users. Therefore, the relying party consumes the claims that are packaged in security tokens that come from users in the claims provider. In other words, a relying party is the organization whose Web servers are protected by the resource-side federation server. The federation server at the relying party uses the security tokens that the claims provider produces to issue tokens to the Web servers that are located in the relying party.

## 相关链接

[Add-AdfsRelyingPartyTrust](./Add-AdfsRelyingPartyTrust.md)

[禁用 AdfsRelyingPartyTrust 功能](./Disable-AdfsRelyingPartyTrust.md)

[ Enable-AdfsRelyingPartyTrust](./Enable-AdfsRelyingPartyTrust.md)

[Remove-AdfsRelyingPartyTrust](./Remove-AdfsRelyingPartyTrust.md)

[Set-AdfsRelyingPartyTrust](./Set-AdfsRelyingPartyTrust.md)

[更新：AdfsRelyingPartyTrust](./Update-AdfsRelyingPartyTrust.md)

