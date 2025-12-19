---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/enable-iissharedconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-IISSharedConfig
---

# 启用 IISSharedConfig

## 摘要
启用共享配置功能。

## 语法

```
Enable-IISSharedConfig [-PhysicalPath] <String> [[-UserName] <String>] [[-Password] <SecureString>]
 [[-KeyEncryptionPassword] <SecureString>] [-DontCopyRemoteKeys] [-Force] [<CommonParameters>]
```

## 描述
`Enable-IISSharedConfig` cmdlet 可以启用 IIS 的共享配置功能。在启用共享配置之前，该操作会先备份相关配置信息（即这些配置对应的键值对）。

您可以通过 IIS Manager 或使用 **Disable-IISSharedConfig** cmdlet 来禁用共享配置。

## 示例

#### 示例 1：启用共享配置
```
PS C:\> $KeyEncryptionPassword = ConvertTo-SecureString -AsPlainText -String "SecurePa$$w0rd" -Force
#For automation scenarios
PS C:\> $KeyEncryptionPassword = Read-Host -AsSecureString
#For UI scenarios
PS C:\> $Password = Read-Host -AsSecureString
PS C:\> Enable-IISSharedConfig -PhysicalPath "C:\export" -KeyEncryptionPassword $KeyEncryptionPassword -UserName "administrator" -Password $Password
```

密码必须采用 **SecureString** 格式。第一个命令使用 `ConvertTo-SecureString` 将指定的密码转换成该格式，然后将其存储在 `$Key Encryption Password` 变量中。在自动化场景中使用 `ConvertTo-SecureString` 非常方便。

第二个命令使用 `Read-Host` 从控制台读取用于密钥加密的密码，然后将其存储在 `$KeyEncryptionPassword` 变量中。在用户界面（UI）场景中，使用 `Read-Host` 是一种更安全的方法。

第三个命令使用 **Read-Host** 来获取具有执行该操作权限的用户账户的密码。

第四条命令允许使用位于 C:\export 目录下的导出配置文件和密钥来进行配置共享。

### 示例 2：在不导入密钥的情况下启用共享配置
```
PS C:\> Enable-IISSharedConfig -PhysicalPath "C:\export" -DontCopyRemoteKeys
```

此命令可以启用配置共享功能，但不会将密钥导入到本地的密钥存储库中。

## 参数

### -DontCopyRemoteKeys
这表示 IIS 会使用当前激活的密钥，并尝试应用由 *PhysicalPath* 参数指定的配置。如果导出的配置中包含使用其他密钥加密的敏感信息，那么 IIS 将无法解密这些敏感信息。

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
强制命令执行，而无需用户确认。

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
指定导出密钥的加密密码。该值最初是通过 `Export-IISConfiguration` cmdlet 或 IIS 管理器设置的。

如果您没有为*DontCopyRemoteKeys*指定值，则必须设置*KeyEncryptionPassword*。如果您为*DontCopyRemoteKeys*指定了值，那么就无法使用这个参数了。

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
指定导出的配置文件和密钥的位置。

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
指定用于访问物理位置的账户的用户名。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.String

### System.security.SecureString

## 输出

### System.Object

## 备注

## 相关链接

[Disable-IISSharedConfig](./Disable-IISSharedConfig.md)

[Get-IISSharedConfig](./Get-IISSharedConfig.md)

