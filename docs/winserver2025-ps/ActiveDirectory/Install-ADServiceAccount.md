---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/install-adserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-ADServiceAccount
---

# 安装 AD 服务账户

## 摘要
在计算机上安装一个由 Active Directory 管理的服务账户，或在计算机上缓存一个组管理的服务账户。

## 语法

```
Install-ADServiceAccount [-WhatIf] [-Confirm] [-AccountPassword <SecureString>] [-AuthType <ADAuthType>]
 [-Force] [-Identity] <ADServiceAccount> [-PromptForPassword] [<CommonParameters>]
```

## 描述
`Install-ADServiceAccount` 这个 cmdlet 用于在运行该 cmdlet 的计算机上安装一个现有的 Active Directory 管理服务账户。该 cmdlet 会验证该计算机是否具备托管该管理服务账户的资格，并在当地进行必要的设置，以便无需用户操作即可管理该管理服务账户的密码。

`Identity` 参数用于指定要安装的 Active Directory 管理服务账户。您可以通过该账户的 distinguished name、GUID、安全标识符 (SID) 或安全帐户管理器 (SAM) 账户名称来识别它。您还可以将此参数设置为某个管理服务账户对象变量（例如 `$<localServiceAccountObject>`），或者通过管道将该管理服务账户对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADServiceAccount` 命令获取一个管理服务账户对象，然后通过管道将其传递给 `Install-ADServiceAccount` 命令进行安装。

`AccountPassword` 参数允许您传递一个包含独立管理服务账户密码的安全字符串；对于组管理的服务账户而言，该参数将被忽略。另外，您也可以使用 `PromptForPassword` 参数来提示用户输入独立管理服务账户的密码。如果您想要安装已配置好的服务账户，则必须提供相应的密码。在将独立管理服务账户安装到位于具有只读域控制器的隔离网络（例如边界网络或 DMZ）中的服务器上时，这一要求尤为必要。在这种情况下，您需要创建该独立管理服务账户，将其与相应的计算机账户关联起来，并为其设置一个易于记忆的密码；在将该账户安装到只读域控制器所在的服务器上时，必须使用这个密码。如果您同时传递了 `AccountPassword` 和 `PromptForPassword` 参数，那么 `AccountPassword` 参数的优先级更高。

## 示例

#### 示例 1：在本地计算机上安装一个托管服务账户
```
PS C:\> Install-ADServiceAccount -Identity 'SQL-HR-svc-01'
```

此命令会在本地计算机上安装一个名为 SQL-HR-svc-01 的托管服务账户。如果使用的是组托管服务账户，则该服务账户必须设置 **PrincipalsAllowedTo RetrieveManagedPassword** 属性。

### 示例 2：获取一个托管服务账户，并将其安装在本地计算机上
```
PS C:\> $Account = Get-ADServiceAccount -Filter "Name -eq 'SQL-HR-svc-01'"
PS C:\> Install-ADServiceAccount $Account
```

该命令从默认目录中获取一个名为 SQL-HR-svc-01 的托管服务账户，并将其安装到本地计算机上。如果使用的是组托管服务账户，则该服务账户必须设置 **PrincipalsAllowedToRetrieveManagedPassword** 属性。

### 示例 3：为只读域控制器站点安装一个独立的管理服务账户
```
PS C:\> Install-ADServiceAccount -Identity 'SQL-HR-svc-01' -PromptForPassword
Please enter the current password for 'CN=SQL-HR-svc-01,CN=Managed Service Accounts,DC=contoso,DC=com'
Password: *******
```

此命令会在一个只读域控制器站点中安装一个名为 SQL-HR-svc-01 的独立托管服务账户。如果使用的是组托管服务账户，则该服务账户必须设置 **Principals AllowedTo RetrieveManagedPassword** 属性。

### 示例 4：使用指定的密码安装一个独立的托管服务账户
```
PS C:\> Install-ADServiceAccount -Identity 'SQL-HR-svc-01' -AccountPassword (ConvertTo-SecureString -AsPlainText "p@ssw0rd" -Force)
```

该命令在只读域控制器站点中安装一个名为 SQL-HR-svc-01 的独立托管服务账户，并将账户密码以安全字符串的形式传递。如果使用的是组托管服务账户，则必须将该服务账户的 `Principals AllowedToRetrieveManagedPassword` 属性设置为启用状态。

## 参数

### -AccountPassword
将账户密码指定为一个安全的字符串。此参数允许您设置已配置的独立管理服务账户的密码，但对于群组管理的服务账户则忽略该参数。当您在具有只读域控制器的隔离网络（站点）上的服务器上安装独立管理服务账户时（例如，边界网络或DMZ），这是必需的操作。在这种情况下，应创建该独立管理服务账户，将其与相应的计算机账户关联起来，并为其设置一个众所周知的密码；在仅能访问只读域控制器而无法访问可写域控制器的服务器上安装此账户时，需要使用该密码。如果您同时传递了*AccountPassword*和*PromptForPassword*参数，则*AccountPassword*参数优先生效。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType
指定要使用的认证方法。该参数的可能取值包括：

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
在运行该cmdlet之前，会提示您进行确认。

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

### -Force
强制安装服务账户。

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

### -Identity
通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A security accounts manager account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个非终止性的错误（即无法继续执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个对象的实例。

```yaml
Type: ADServiceAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PromptForPassword
这表示您可以输入一个预先创建的独立管理服务账户的密码。对于属于组管理的托管服务账户而言，这个密码是可选的（即可以不使用）。当您需要在位于隔离网络环境中的服务器上安装独立管理服务账户时（例如：该网络环境中没有可写权限的域控制器，只有只读域控制器（RODC）），就需要使用这种方式。在这种情况下，您需要创建该独立管理服务账户，将其与相应的计算机账户关联起来，并为其指定一个明确的密码；在仅包含 RODC 的服务器上安装该账户时，必须提供这个密码。如果您同时提供了 `AccountPassword` 和 `PromptForPassword` 两个参数，那么 `AccountPassword` 参数的优先级会更高。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.ADServiceAccount
由*Identity*参数接收一个托管服务账户对象。

## 输出

### 无

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* This cmdlet must be run from an elevated PowerShell session.
* To successfully install a managed service account, the service account should have the *PrincipalsAllowedToRetrieveManagedPassword* parameter option set first by using either the New-ADServiceAccount or Set-ADServiceAccount cmdlet first. Otherwise, installation will fail.

## 相关链接

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Remove-ADServiceAccount](./Remove-ADServiceAccount.md)

[重置 AD 服务账户密码](./Reset-ADServiceAccountPassword.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)

[卸载 ADServiceAccount](./Uninstall-ADServiceAccount.md)
