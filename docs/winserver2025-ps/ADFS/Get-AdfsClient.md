---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsClient
---

# Get-AdfsClient

## 摘要
检索OAuth 2.0客户端的注册信息。

## 语法

### 名称（默认值）
```
Get-AdfsClient [[-Name] <String[]>] [<CommonParameters>]
```

### ClientId
```
Get-AdfsClient [-ClientId] <String[]> [<CommonParameters>]
```

### InputObject
```
Get-AdfsClient [-InputObject] <AdfsClient> [<CommonParameters>]
```

## 描述
`Get-AdfsClient` cmdlet 可以检索之前在 Active Directory Federation Services (AD FS) 中注册的 OAuth 2.0 客户端的注册信息。

## 示例

### 示例 1：检索所有客户的注册信息
```
PS C:\> Get-AdfsClient



RedirectUri : {ms-app://windows.immersivecontrolpanel/}
Name        : Device Registration Client
Description : Client for the Device Registration Service
ClientId    : dd762716-544d-4aeb-a526-687b73838a22
BuiltIn     : True
Enabled     : True
ClientType  : Public

RedirectUri : {https://168f3ee4-63fc-4723-a61a-6473f6cb515c/redir}
Name        : Windows Server Work Folders Client
Description : Client for syncing user files to a Work Folders sync share
ClientId    : 168f3ee4-63fc-4723-a61a-6473f6cb515c
BuiltIn     : True
Enabled     : True
ClientType  : Public
```

此命令用于检索当前在 AD FS 中注册的所有 OAuth 2.0 客户端的注册信息。

### 示例 2：根据客户端名称检索注册信息
```
PS C:\> Get-AdfsClient -Name "Device Registration Client"



RedirectUri : {ms-app://windows.immersivecontrolpanel/}
Name        : Device Registration Client
Description : Client for the Device Registration Service
ClientId    : dd762716-544d-4aeb-a526-687b73838a22
BuiltIn     : True
Enabled     : True
ClientType  : Public
```

此命令用于检索名为“Device Registration Client”的OAuth 2.0客户的注册信息。

### 示例 3：通过客户端 ID 检索注册信息
```
PS C:\> Get-AdfsClient -ClientId "dd762716-544d-4aeb-a526-687b73838a22"



RedirectUri : {ms-app://windows.immersivecontrolpanel/}
Name        : Device Registration Client
Description : Client for the Device Registration Service
ClientId    : dd762716-544d-4aeb-a526-687b73838a22
BuiltIn     : True
Enabled     : True
ClientType  : Public
```

该命令用于检索由客户端标识符 dd762716-544d-4aeb-a526-687b73838a22 指定的 OAuth 2.0 客户端的注册信息。

## 参数

### -ClientId
指定一个客户端标识符数组，用于获取 해당 OAuth 2.0 客户端的注册信息。

```yaml
Type: String[]
Parameter Sets: ClientId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定一个类型为 **AdfsClient** 的对象，该对象表示用于获取注册信息的 OAuth 2.0 客户端。

```yaml
Type: AdfsClient
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定要检索注册信息的 OAuth 2.0 客户端的名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *ClientId* 和 *Name* 参数被接收。

### MicrosoftIdentityServer.Management Resources.AdfsClient

`AdfsClient` 对象是通过 `InputObject` 参数接收到的。

## 输出

### MicrosoftIdentityServer.Management Resources.AdfsClient

返回一个或多个 AdfsClient 对象，这些对象代表用于联合服务的 Adfs 客户端。

## 备注

## 相关链接

[Add-AdfsClient](./Add-AdfsClient.md)

[禁用 AdfsClient](./Disable-AdfsClient.md)

[Enable-AdfsClient](./Enable-AdfsClient.md)

[Remove-AdfsClient](./Remove-AdfsClient.md)

[Set-AdfsClient](./Set-AdfsClient.md)

