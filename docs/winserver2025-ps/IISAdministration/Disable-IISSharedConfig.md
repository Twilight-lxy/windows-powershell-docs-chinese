---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/disable-iissharedconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-IISSharedConfig
---

# 禁用 IISSharedConfig

## 摘要
禁用 IIS 共享配置。

## 语法

```
Disable-IISSharedConfig [-DontRestoreBackedUpKeys] [-CopyRemoteConfigToLocalFiles] [<CommonParameters>]
```

## 描述
` Disable-IISSharedConfig` 这个cmdlet会禁用IIS的共享配置功能，并恢复到启用共享配置时备份的配置设置。同时，IIS也会重新使用在启用共享配置之前使用的本地 `applicationHost.config` 文件。

您可以通过 IIS 管理器用户界面或 **Enable-IISSharedConfig** cmdlet 来启用共享配置功能。

如果由于某种原因没有备份密钥，该cmdlet会执行失败并显示警告信息。在这种情况下，如果你想禁用共享配置功能，可以使用*DontRestoreBackedUpKeys*参数。

## 示例

### 示例 1：禁用共享配置并恢复密钥
```
PS C:\> Disable-IISSharedConfig
```

此命令会禁用共享配置。随后，IIS会使用位于 %WINDIR%\config 目录下的 local applicationHost.config 文件。备份的配置信息会被恢复到本地配置存储中，然后被删除。

### 示例 2：禁用共享配置（无需恢复密钥）
```
PS C:\> Disable-IISSharedConfig -DontRestoreBackedUpKeys
```

此命令会禁用共享配置。之后，IIS将使用位于 %WINDIR%\config 目录下的 local applicationHost.config 文件。所有被备份的配置信息都会被删除，并且不会被恢复。

### 示例 3：禁用共享配置并在本地使用该配置
```
PS C:\> Disable-IISSharedConfig -CopyRemoteConfigToLocalFiles
```

此命令会禁用共享配置功能。IIS会将共享配置复制到本地并使用该配置；同时，备份的密钥将被删除且不会被恢复。

## 参数

### -CopyRemoteConfigToLocalFiles
在禁用共享配置之前，请将远程配置内容复制到本地版本的 `applicationHost.config` 文件中。

在启用共享配置之前使用的 `applicationHost.config` 文件版本会被覆盖。同时，备份密钥也会被删除，因为这些密钥只能用于被覆盖后的 `applicationHost.config` 文件版本。

IIS 仍然使用那些在共享配置模式下有效的工作键，而这些共享配置现在已被替换为本地配置。

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

### -DontRestoreBackedUpKeys
这表示该操作不会恢复备份的配置信息。如果您没有指定“CopyRemoteConfigToLocalFiles”参数，IIS会重新使用其本地版本的 `applicationHost.config` 文件，并使用当前有效的配置信息来进行共享配置的管理。

如果 `applicationHost.config` 文件的本地副本中包含用当前未激活的密钥加密的敏感信息，IIS 将无法解密这些信息。因此，您必须重新输入并重新加密这些敏感信息，以便依赖于它们的功能能够正常运行。

*DontRestoreBackedUpKeys* 在以下场景中非常有用：备份密钥已被删除，但 IIS 管理员仍希望禁用共享配置功能。

如果您指定了“CopyRemoteConfigToLocalFiles”参数，那么这个参数将被忽略，因为在那种情况下备份的密钥不会被恢复。无论如何，当共享配置被禁用时，备份的密钥将会被删除。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Enable-IISSharedConfig](./Enable-IISSharedConfig.md)

[Get-IISSharedConfig](./Get-IISSharedConfig.md)

