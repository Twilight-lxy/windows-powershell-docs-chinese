---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/export-iisconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-IISConfiguration
---

# 导出 IIS 配置

## 摘要
导出 IIS 配置文件和机器密钥。

## 语法

```
Export-IISConfiguration [-PhysicalPath] <String> [[-UserName] <String>] [[-Password] <SecureString>]
 [[-KeyEncryptionPassword] <SecureString>] [-DontExportKeys] [-Force] [<CommonParameters>]
```

## 描述
`Export-IISConfiguration` cmdlet 将 IIS 配置信息和机器密钥导出到指定的位置。

导出的配置文件仅对管理员可见，且需要通过访问控制列表（ACL）进行授权才能访问。

你可以使用 *KeyEncryptionPassword* 参数来加密机器密钥。

您必须提供一个有效的用户名和密码才能访问导出位置。如果您不想导出密钥，请指定 *DontExportKeys* 参数。

## 示例

### 示例 1：导出配置文件
```
PS C:\> $KeyEncryptionPassword = ConvertTo-SecureString -AsPlainText -String "SecurePa$$w0rd" -Force
#Automation scenarios
PS C:\> $KeyEncryptionPassword = Read-Host -AsSecureString
#UI scenarios
PS C:\> Export-IISConfiguration -PhysicalPath "C:\export" -KeyEncryptionPassword $keyEncryptionPassword
PS C:\> Export-IISConfiguration -PhysicalPath "C:\export" -DontExportKeys -Force
```

密码必须采用 **SecureString** 格式。第一个命令使用 `ConvertTo-SecureString` 将指定的密码转换成安全字符串，然后将其存储在 `$KeyEncryptionPassword` 变量中。在自动化场景中使用 `ConvertTo-SecureString` 非常有用。

第二个命令使用 `Read-Host` 来读取用户通过控制台输入的密钥加密密码，并将其存储在 `$KeyEncryptionPassword` 变量中。在用户界面（UI）场景中使用 `Read-Host` 是一种更安全的方法。

第三个命令将密钥和配置信息导出到 C:\export 目录，并使用指定的密码对密钥进行加密。

第四条命令会导出配置文件，但不会包含配置项的键值对。由于指定了“Force”参数，这条命令会覆盖之前的配置文件。被导出的配置文件（位于C:\export目录中）中的配置项并不会被删除。

## 参数

### -DontExportKeys
表示此操作不会导出密钥。

要使用此导出的配置启用 IIS 共享配置功能，请运行带有 *DontCopyRemoteKeys* 参数的 **Enable-IISSharedConfig** cmdlet。

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

### -Force
强制命令运行，而不需要用户确认。

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

### -KeyEncryptionPassword
指定用于导出密钥的密钥加密密码。

您可以使用这个值与 `Enable-IISSharedConfig` 一起使用，以便启用与该 cmdlet 导出的配置共享的配置。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Password
指定用于访问该物理位置的账户的密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PhysicalPath
指定用于导出配置和密钥的目标位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UserName
指定用于访问该物理位置的账户的用户名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Security.SecureString

## 输出

### System.Object

## 备注

## 相关链接

