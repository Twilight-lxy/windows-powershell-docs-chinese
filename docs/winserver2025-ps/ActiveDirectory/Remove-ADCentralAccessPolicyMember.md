---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adcentralaccesspolicymember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADCentralAccessPolicyMember
---

# 删除 ADCentralAccessPolicy 成员

## 摘要
从 Active Directory 中的中央访问策略中删除中央访问规则。

## 语法

```
Remove-ADCentralAccessPolicyMember [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADCentralAccessPolicy> [-Members] <ADCentralAccessRule[]> [-PassThru] [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Remove-ADCentralAccessPolicyMember` cmdlet 用于从 Active Directory 中的中央访问策略中删除相应的中央访问规则。

## 示例

### 示例 1：从中央访问策略中删除资源属性
```
PS C:\> Remove-ADCentralAccessPolicyMember -Identity "Finance Policy" -Members "Finance Documents Rule"
```

此命令会从名为“Finance Policy”的中央访问策略中删除名为“Finance Documents Rule”的资源属性。

### 示例 2：从中心访问策略中删除中央访问规则
```
PS C:\> Remove-ADCentralAccessPolicyMember -Identity "Finance Policy" -Members "Finance Documents Rule","Corporate Documents Rule"
```

该命令从中央访问策略“Finance Policy”中删除了名为“Finance Documents Rule”和“Corporate Documents Rule”的两条中央访问规则。

### 示例 3：使用过滤器获取中央访问策略，然后从这些策略中移除指定的中央访问规则
```
PS C:\> Get-ADCentralAccessPolicy -Filter "Name -like 'Corporate*'" | Remove-ADCentralAccessPolicyMember -Members "Finance Documents Rule","Corporate Documents Rule"
```

这个命令会获取那些名称中以“Corporate”开头的中央访问策略，然后将获取到的结果传递给**Remove-ADCentralAccessPolicyMember**命令。该命令会从这些策略中删除名为“Finance Documents Rule”和“Corporate Documents Rule”的中央访问规则。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

```yaml
Type: ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行任务的代理组件没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性在轻量级目录访问协议（LDAP）中的显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADCentralAccessPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Members
Specifies a set of central access rule (CAR) objects in a comma-separated list to add to a central access policy.

To identify each object, use one of the following property values:

- Name
- A distinguished name
- GUID (objectGUID)

Note: The identifier in parentheses is the LDAP display name.

You can also provide objects to this parameter directly.

```yaml
Type: ADCentralAccessRule[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供一个相应的域名或目录服务器的名称。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列任意一种方式指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，确定顺序按照列出的顺序进行：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无，或为 Microsoft.ActiveDirectory.Management.ADCentralAccessPolicy
`Identity` 参数接收一个 `ADCentralAccessPolicy` 对象。

## 输出

### 无值或 Microsoft ActiveDirectory.ADCentralAccessPolicy
当指定了*PassThru*参数时，此cmdlet会返回修改后的**ADCentralAccessPolicy**对象。默认情况下，该cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with a read-only domain controller.
* This cmdlet does not work with an Active Directory snapshot.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Add-ADCentralAccessPolicyMember](./Add-ADCentralAccessPolicyMember.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

