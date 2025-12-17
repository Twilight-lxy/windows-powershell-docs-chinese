---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsendpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsEndpoint
---

# Get-AdfsEndpoint

## 摘要
从 AD FS 中检索一个端点。

## 语法

### 地址（默认值）
```
Get-AdfsEndpoint [[-AddressPath] <String[]>] [<CommonParameters>]
```

### FullUrl
```
Get-AdfsEndpoint [-FullUrl] <Uri[]> [<CommonParameters>]
```

## 描述
`Get-AdfsEndpoint` cmdlet 用于从 Active Directory Federation Services (AD FS) 中检索指定的端点。`AdfsEndpoint` 对象的集合包含了服务器上所有支持的端点信息。您可以使用这个列表来查看端点的配置，并启用或禁用它们。若要查看完整的端点列表，可以不带任何参数使用该 cmdlet。

## 示例

### 示例 1：获取一个端点
```
PS C:\> Get-AdfsEndpoint -AddressPath "/adfs/services/trust/13/Windows"
```

这个命令用于获取 WS-Trust 1.3 终点。

## 参数

### -AddressPath
指定一个不包含 AD FS 服务名称的地址路径数组。该 cmdlet 会获取与所指定路径对应的终端点。例如，这样的路径可以是 `/adfs/portal/updatepassword`。

```yaml
Type: String[]
Parameter Sets: Address
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -FullUrl
指定用于检索的端点的完整URL。

```yaml
Type: Uri[]
Parameter Sets: FullUrl
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]
System Uri[]

## 输出

### Microsoft IdentityServer.ManagementResources Endpoint
```json
AddressPath           : string
ClientCredentialType    : string
Enabled              : bool
FullUrl               : uri
Protocol             : string
Proxy                : bool
SecurityMode         : string
Version              : string
```
```

### MicrosoftIdentityServer.PowerShell.Resources.Endpoint
此cmdlet返回一个类结构，该结构表示Federation Service的端点信息。

## 备注
* Endpoints provide access to the federation server functionality of AD FS, such as token issuance and the publication of federation metadata. Depending on the type of endpoint, you can enable or disable the endpoint or control whether the endpoint is published to Web Application Proxy.

## 相关链接

[ Disable-AdfsEndpoint](./Disable-AdfsEndpoint.md)

[Enable-AdfsEndpoint](./Enable-AdfsEndpoint.md)

[Set-AdfsEndpoint](./Set-AdfsEndpoint.md)

